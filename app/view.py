from app import app
from flask import render_template

from posts.forms import LoginForm

from admin.admin_ckeditor_upload_view import upload


@app.route('/')
def index():
    return render_template('index.html')
