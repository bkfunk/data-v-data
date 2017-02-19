from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    """Model for a user, who can create experiments as well as answer questions"""
    id = db.Column(db.Integer, primary_key=True)
    # Profile settings
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(128))
    created_at = db.Column(db.DateTime)
    # Relationships
    experiments = db.relationship('Experiment', backref='author', lazy='dynamic')
    # attempts = db.relationship('Attempt', backref='attempts', lazy='dynamic')

    def __init__(self, email, first_name=None, last_name=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.utcnow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    # @property
    # def is_authenticated(self):
    #     return True
    #
    # @property
    # def is_active(self):
    #     return True
    #
    # @property
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #     try:
    #         return unicode(self.id)  # python 2
    #     except NameError:
    #         return str(self.id)  # python 3

    def add_experiment(self, experiment):
        self.experiments.append(experiment)

    def __repr__(self):
        return '<User %r>' % (self.email)


class Experiment(db.Model):
    """An experiment is a collection of:
    - Figures to test
    - Attributes to test for each figure
    """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    figures = db.relationship('Figure', backref='experiment', lazy = 'dynamic')

    def __init__(self, name, user):
        self.name = name
        self.author = user


class Figure(db.Model):
    """A single figure (e.g. plot), as part of an experiment"""
    id = db.Column(db.Integer, primary_key = True)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id'))
    # img

#
# class Attribute(db.Model):
#     # Proportion
#     # Value
#     # Comparative Value (is A > B)
#     # Trend (is A increasing or decreasing, or flat)
#     # Novelty/Outlier (is A new? is A unusual?)
#
#     pass
#
#
# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     text = db.Column(db.String(512))
#     # options = set of options
#     # answer = correct answer
#
#
# class Attempt(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     # user id
#     # time presented
#     # time answered
#     # question id
#     # chosen option
#     # correct?
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post %r>' % (self.body)










# class Test(db.Model)
#     """set of plots and questions? attempts?"""
#     # attributes to test
#     pass
