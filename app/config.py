import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:microlab0315@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'a76b1ab91c4859767409975642750b85f1d61dac'

    # FLASK-SECURITY
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    LANGUAGES = ['ru']

    # CKEditor
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_FILE_UPLOADER = 'upload'
    # CKEDITOR_ENABLE_CSRF = True  # if you want to enable CSRF protect, uncomment this line
    UPLOADED_PATH = os.path.join(basedir, 'uploads')
