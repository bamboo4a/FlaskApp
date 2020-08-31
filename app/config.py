import os

class Configuration(object):
    # App
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:###@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '####'

    # FLASK-SECURITY
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    LANGUAGES = ['ru']

    # CKEditor
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_FILE_UPLOADER = 'upload'

    # Cloudinary
    os.environ['CLOUDINARY_URL'] = '########'
    CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
