from django.apps import AppConfig
#from app.jobs import updater

#execute_task = updater.Scheduler()

class MainConfig(AppConfig):
    name = 'app'

    def ready(self):
        pass
        #execute_task.start()