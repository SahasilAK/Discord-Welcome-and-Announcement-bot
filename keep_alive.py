from flask import Flask, request, render_template
from threading import Thread
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
import os
from flask_login import current_user
import json


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                         Length(min=8)])
    submit = SubmitField(label='Log In')


class AnnounceForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    desc = TextAreaField(label="Description")
    link = StringField(label="Url")
    image_link = StringField(label="Url for Image")
    a_submit = SubmitField(label='Announce')


app = Flask('')
app.secret_key = os.getenv('SECRET_KEY')
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.username.data == os.getenv(
                'USERNAME') and login_form.password.data == os.getenv(
                    'PASSWORD'):
            return render_template('success.html',form={'done':'What are you going to Announce today'})
        else:
            return render_template('denied.html', cure)

    return render_template('login.html', form=login_form)


@app.route("/announce", methods=["POST", "GET"])
def announce():
    announce_form = AnnounceForm()
    if announce_form.validate_on_submit():
        a_title = announce_form.title.data
        a_desc = announce_form.desc.data
        a_link = announce_form.link.data
        a_img = announce_form.image_link.data
        update_anounce(a_title, a_desc, a_link, a_img)

        return render_template('success.html', form={'done':'Announced'})

    return render_template('announce.html', form=announce_form)


def update_anounce(title, desc, link, img):
    announce_data = {
        'title': title,
        'description': desc,
        'url': link,
        'img_url': img
    }
    with open('data.json','w') as data_file:
      json.dump(announce_data,data_file)


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
