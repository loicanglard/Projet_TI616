import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-prod')
    DATABASE = os.environ.get('DATABASE_URL', 'database/trailmemoire.db')
    DEBUG = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    WTF_CSRF_ENABLED = True
