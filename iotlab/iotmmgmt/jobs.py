from django.conf import settings
from iotmmgmt.models import *
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from subprocess import Popen, PIPE
from datetime import datetime

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, 'cron', minute='*', replace_existing=True)
def test_job():
  print(datetime.now())
  p = Popen(settings.IOTMMGMT_SCRIPT, shell=True, stdout=PIPE, stderr=PIPE)
  p.wait()
  res = p.communicate() 
  print(res)

register_events(scheduler)

scheduler.start()
print("Scheduler started!")
