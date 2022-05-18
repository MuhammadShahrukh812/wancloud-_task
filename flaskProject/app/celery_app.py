from celery import Celery

celery = Celery('app', broker='amqp://guest:guest@rabbitmq:5672//', include=['app.celery_task'])
