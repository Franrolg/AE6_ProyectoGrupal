from django.apps import AppConfig


class Grupal6Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grupal6'

    def ready(self):
        import grupal6.signal
