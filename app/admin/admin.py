from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import current_user
from flask import redirect, url_for, request
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, Length


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'tags', 'body', 'img_card']
    column_searchable_list = ('title',)
    column_default_sort = ('created', True)
    form_overrides = dict(body=CKEditorField)
    form_args = {
        'title': {
            'label': 'Заголовок',
            'validators': [DataRequired(), Length(min=5, max=140)]
        },
        'body': {
            'label': 'Текст',
            'validators': [DataRequired()]
        },
        'tags': {
            'label': 'Тег',
            'validators': []
        }
    }

    # Вывод первых 20 символов в поле 'body'
    def _body_formatter(view, context, model, name):
        return model.body[:20]

    column_formatters = {
        'body': _body_formatter,
    }


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name']
    form_args = {
        'name': {
            'label': 'Название'
        }
    }
