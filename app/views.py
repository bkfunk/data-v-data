from flask import render_template, redirect, url_for, session, g, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, google, lm, db
from .models import User

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    user = g.user
    return render_template(
        'index.html',
        title="Home",
        user = user
    )
    # access_token = session.get('access_token')
    # if access_token is None:
    #     return redirect(url_for('login'))
    #
    # access_token = access_token[0]
    # from urllib2 import Request, urlopen, URLError
    #
    # headers = {'Authorization': 'OAuth '+access_token}
    # req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
    #               None, headers)
    # try:
    #     res = urlopen(req)
    # except URLError, e:
    #     if e.code == 401:
    #         # Unauthorized - bad token
    #         session.pop('access_token', None)
    #         return redirect(url_for('login'))
    #     return res.read()
    #
    # return res.read()

@app.route('/login')
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    return google.authorize(callback = url_for(
        'authorized',
        _external=True#,
        #next=request.args.get('next') or request.referrer or None
        )
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route(app.config['REDIRECT_URI'])
@google.authorized_handler
def authorized(resp):
    next_url = request.args.get('next') or url_for('index')

    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['access_token'] = (
        resp['access_token'], ''
    )



    # access_token = session.get('access_token')
    # if access_token is None:
    #     return redirect(url_for('login'))
    #
    # access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError
    import json
    #
    headers = {'Authorization': 'OAuth '+resp['access_token']}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()
    #
    # return res.read()
    google_user = json.loads(res.read())

    if google_user.get('email') is None or google_user.get('email') == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))

    user = User.query.filter_by(email=google_user.get('email')).first()
    if user is None:
        flash("No such user", 'error')
        nickname = google_user.get('nickname')
        if nickname is None or nickname == "":
            nickname = google_user.get('email').split('@')[0]
        user = User(nickname=nickname, email=google_user.get('email'))
        db.session.add(user)
        db.session.commit()

    login_user(user)
    flash('You were signed in as %s' % user.nickname)

    return redirect(next_url)
    #
    # access_token = resp['access_token']
    # session['access_token'] = access_token, ''
    # return redirect(url_for('index'))
