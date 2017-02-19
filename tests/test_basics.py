import pytest
from flask import current_app
# from app import create_app, db




def test_app_exists(basic_app):
    print("TEST APP EXISTS")
    assert current_app is not None

def test_app_is_testing(basic_app):
    assert current_app.config['TESTING']

# class BasicTestCase(unittest.TestCase):
#     def setup(self):
#         self.app = create_app('testing')
#     def teardown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()
#
#     def test_app_exists(self):
#         self.assert_false(current_app is None)
#
#     def test_app_is_testing(self):
#         self.assert_true(current_app.config['TESTING'])
