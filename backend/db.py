import sqlite3
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        g.db.execute('PRAGMA foreign_keys = ON')
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db(app):
    app.teardown_appcontext(close_db)

    # Auto-initialisation au démarrage (CREATE TABLE IF NOT EXISTS = sans danger)
    with app.app_context():
        db = get_db()
        with app.open_resource('database/schema.sql') as f:
            db.executescript(f.read().decode('utf8'))

    @app.cli.command('init-db')
    def init_db_command():
        db = get_db()
        with current_app.open_resource('database/schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        click.echo('Base de données initialisée.')

    @app.cli.command('reset-db')
    def reset_db_command():
        db = get_db()
        # Désactiver les FK pour pouvoir drop dans n'importe quel ordre
        db.execute('PRAGMA foreign_keys = OFF')
        tables = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
        for table in tables:
            db.execute(f'DROP TABLE IF EXISTS {table["name"]}')
        db.execute('PRAGMA foreign_keys = ON')
        
        with current_app.open_resource('database/schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        click.echo('Base de données réinitialisée.')
