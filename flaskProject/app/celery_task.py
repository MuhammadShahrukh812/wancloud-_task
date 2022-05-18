from app.celery_app import celery
from celery.schedules import crontab
from app import models

celery.conf.beat_schedule = {
    "run_every_minute":
        {"task": "add",
         "schedule": crontab(hour=10, minute=0),
         "args": str(1),
         },

}

celery.conf.timezone = 'UTC'


@celery.task(bind=True, name="add")
def add(x):
    print('hello')



