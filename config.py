class BaseConfiguration(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'flask-session-insecure-secret-key'
    HASH_ROUNDS = 100000

class TestConfiguration(BaseConfiguration):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    HASH_ROUNDS = 1
