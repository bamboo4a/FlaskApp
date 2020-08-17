from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import current_user
from flask import redirect, url_for, request
from posts.wysiwyg import CKTextAreaField


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
    form_columns = ['title', 'body']
    extra_js = ['https://cdn.ckeditor.com/4.14.1/standard/ckeditor.js']
    form_overrides = dict(body=CKTextAreaField)


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name']