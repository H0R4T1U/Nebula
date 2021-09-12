from django.apps import AppConfig


class NebulaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Nebula'

    def ready(self):
        from githubUpdater import updater
        updater.start() #CHEECH IMPLEMENTATION
        