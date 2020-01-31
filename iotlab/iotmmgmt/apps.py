from django.apps import apps, AppConfig

class IotmmgmtConfig(AppConfig):
  name = 'iotmmgmt'

  scheduler = None
  def ready(self):
    if self.scheduler is None:
      self.scheduler = BackgroundScheduler()
      self.scheduler.add_job(run, trigger='cron', minute='*')
      self.scheduler.start()
