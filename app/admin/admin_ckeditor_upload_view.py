from app import app
from flask import send_from_directory, request, url_for
from flask_ckeditor import upload_fail, upload_success
# ___________________________
from cloudinary.uploader import upload as up_to_cloud
from cloudinary.utils import cloudinary_url


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['upload']
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg', 'webp']:
        return upload_fail(message='Image only!')
    result = up_to_cloud(f)
    url = result['url']
    return upload_success(url=url)
