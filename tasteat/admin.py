from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import models

admin = Admin(name='tasteat', template_mode='bootstrap3')


def configure_admin(app):
    admin.init_app(app)
    # admin.add_view(ModelView(models.Ingredient))
