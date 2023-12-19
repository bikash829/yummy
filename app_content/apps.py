from django.apps import AppConfig


class AppContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_content'
    verbose_name = 'Site Content'

    # order = ['SiteMenu', 'Section', 'About']

