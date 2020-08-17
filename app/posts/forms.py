from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask_ckeditor import CKEditorField

from flask_wtf import FlaskForm


class PostForm(Form):
    title = StringField('Заголовок')
    body = CKEditorField('Содержание')


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email()])
    psw = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100)])
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')
