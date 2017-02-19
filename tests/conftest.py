"""Test fixtures"""
import pytest
from app import models

class AppInstance:
    def __init__(self):
        print("INIT APP INSTANCE")
        from app import create_app, db
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db
        self.db.create_all()

    def teardown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()


@pytest.fixture(scope='module')
def basic_app():
    '''Basic empty testing app'''
    print("SETUP BASIC APP")
    basic_app = AppInstance()
    yield basic_app
    print("TEAR DOWN BASIC APP")
    basic_app.teardown()

@pytest.fixture(scope='module')
def ipsum_app():
    '''App with random data in database'''
    ipsum_app = AppInstance()
    ipsum_app.db.session.add(models.User('foo@bar.com'))
    yield ipsum_app
    ipsum_app.teardown()
