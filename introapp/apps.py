from django.apps import AppConfig

class IntroappConfig(AppConfig):
    name = 'introapp'

    def ready(self):
        import introapp.signals
