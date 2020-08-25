from app import app
from flask import send_from_directory, request, url_for
from flask_ckeditor import upload_fail, upload_success
import os
from pathlib import Path
from datetime import datetime
from config import Configuration


def get_path():
    time_now = datetime.now()
    path = Path.joinpath(Configuration.UPLOADED_PATH, str(time_now.year)[:2], str(time_now.month), str(time_now.day))
    return path


@app.route('/files/<filename>')
def uploaded_files(filename):
    path = get_path()
    return send_from_directory(path, filename)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')

    # получение адреса
    directory_now = get_path()
    if not directory_now.exists():
        directory_now.mkdir(parents=True, exist_ok=True)
    f.save(Path.joinpath(directory_now, f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)


