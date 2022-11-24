from celery import Celery

import os

from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")
app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every week (monday 8a.m.) list of new posts sender': {
        'task': 'news.tasks.weekly_sender',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday')
    }
}