import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-prod')
    # Sur Render/Vercel seul /tmp est inscriptible ; en local on garde le chemin habituel
    _default_db = '/tmp/trailmemoire.db' if os.environ.get('RENDER') or os.environ.get('VERCEL') else 'database/trailmemoire.db'
    DATABASE = os.environ.get('DATABASE_URL', _default_db)
    DEBUG = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    WTF_CSRF_ENABLED = True
