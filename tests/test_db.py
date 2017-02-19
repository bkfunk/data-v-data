import pytest
from app import models

def test_ipsum_app_exists(ipsum_app):
    from flask import current_app
    assert current_app is not None

def test_ipsum_app_has_users(ipsum_app):
    users = models.User.query.all()
    print(users)
    assert users is not None
