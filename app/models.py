from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Plot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # img


class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(512))
    # options = set of options
    # answer = correct answer



class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # user id
    # time presented
    # time answered
    # question id
    # chosen option
    # correct?


class Test(db.Model)
    """set of plots and questions? attempts?"""
    # attributes to test
    pass


class Attribute(db.Model)
    # Proportion
    # Value
    # Comparative Value (is A > B)
    # Trend (is A increasing or decreasing, or flat)
    # Novelty/Outlier (is A new? is A unusual?)

    pass
