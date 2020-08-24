from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from admin.admin import *
from flask_babelex import Babel
from flask_ckeditor import CKEditor

# app
app = Flask(__name__)
app.config.from_object(Configuration)

# translation
babel = Babel(app, 'ru')

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ADMIN
from models import *
admin = Admin(app, 'На главную', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))


# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# CKEditor

ckeditor = CKEditor(app)
