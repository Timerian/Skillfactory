import datetime

from celery import shared_task
import time

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post


@shared_task
def hello():
    time.sleep(10)
    print('Hello, world')


@shared_task
def postcreate_notify(pid):
    post = Post.objects.get(id=pid)
    for category in post.categories.all():
        for user in category.subscribers.all():
            html_content = render_to_string(
                'newpub_mail.html',
                {
                    'post': post,
                    'user': user
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'{post.head}',
                body=post.text,
                from_email='timerian.music@yandex.ru',
                to=[user.email]
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

@shared_task
def weekly_sender():
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