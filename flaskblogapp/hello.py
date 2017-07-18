from flask import Flask, render_template, session, redirect, url_for
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')
# @app.route('/')
# def index():
#     return '<h1>Hello flask!</h1>'

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>your browser is %s!</p>' % user_agent

# @app.route('/')
# def index():
#     return '<h1>Bad Request!</h1>', 400

# @app.route('/')
# def index():
#     response = make_response('<h1>this document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response


# @app.route('/')
# def index():
#     return redirect('https://www.baidu.com')


# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
        # name = form.name.data
        # form.name.data = ''
    return render_template('index.html', form=form, name=session.get('name'))


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
