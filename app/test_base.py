from flask_testing import TestCase

from . import app

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfiguration')
        return app
