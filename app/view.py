from app import app
from flask import render_template

from posts.forms import LoginForm


@app.route('/')
def index():
    return render_template('index.html')



