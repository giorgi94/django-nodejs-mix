from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BlogConfig(AppConfig):
    label = 'blog'
    name = 'apps.blog'
    verbose_name = _('Blog')
