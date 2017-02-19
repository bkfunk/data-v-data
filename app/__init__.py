from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_oauth import OAuth
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from config import config


bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# oauth = OAuth()

# remote_apps = {}


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    nav.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # remote_apps['google'] = oauth.remote_app('google',
    #                           base_url='https://www.google.com/accounts/',
    #                           authorize_url='https://accounts.google.com/o/oauth2/auth',
    #                           request_token_url=None,
    #                           request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
    #                                                 'response_type': 'code'},
    #                           access_token_url='https://accounts.google.com/o/oauth2/token',
    #                           access_token_method='POST',
    #                           access_token_params={'grant_type': 'authorization_code'},
    #                           consumer_key=app.config['GOOGLE_CLIENT_ID'],
    #                           consumer_secret=app.config['GOOGLE_CLIENT_SECRET'])

    return app
#
# Bootstrap(app)
#
# nav = Nav()
#
# nav.init_app(app)
#
# db = SQLAlchemy(app)
#
# lm = LoginManager()
# lm.init_app(app)
#
# lm.login_view = 'login'
#
# oauth = OAuth()





# from app import views, models
