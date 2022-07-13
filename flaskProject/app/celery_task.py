from app.celery_app import celery
from datetime import timedelta

celery.conf.beat_schedule = {
    "run_every_minute":
        {"task": "add",
         "schedule": timedelta(seconds=5),

         },

}

celery.conf.timezone = 'UTC'


@celery.task(bind=True, name="add")
def add(x):
    print('hello')
