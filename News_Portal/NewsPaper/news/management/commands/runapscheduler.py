import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

import datetime

from news.models import Post

logger = logging.getLogger(__name__)


def my_job():
    today = datetime.datetime.today()
    week_ago = today - datetime.timedelta(7)
    post_list = Post.objects.filter(time_add__gt=week_ago)
    users = User.objects.all()

    for user in users:
        user_categories = user.categories.all()
        user_post_list = post_list.filter(categories__in=user_categories)

        html_content = render_to_string(
            'weeklysend_mail.html',
            {
                'post_list': user_post_list,
                'username': user.username,
                'categories': user_categories
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'Publications for the week',
            body=f'{user.username}',
            from_email='timerian.music@yandex.ru',
            to=[user.email]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    print('fuck yeah')


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(minute="*/1"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")