from django.core.mail import EmailMultiAlternatives, mail_managers
from django.db.models.signals import m2m_changed, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post


# @receiver(m2m_changed, sender=Post.categories.through)
# def postcreate_notify(instance, sender, **kwargs):
#     for category in instance.categories.all():
#         for user in category.subscribers.all():
#             html_content = render_to_string(
#                 'newpub_mail.html',
#                 {
#                     'post': instance,
#                     'user': user
#                 }
#             )
#             msg = EmailMultiAlternatives(
#                 subject=f'{instance.head}',
#                 body=instance.text,
#                 from_email='timerian.music@yandex.ru',
#                 to=[user.email]
#             )
#             msg.attach_alternative(html_content, 'text/html')
#             msg.send()


@receiver(post_delete, sender=Post)
def postdelete_notify(instance, sender, **kwargs):
    html_content = render_to_string(
        'postdelete_mail.html',
        {
            'post': instance,

        }
    )
    mail_managers(
        subject=f'{instance.head} ({instance.author}).',
        message=f'Publication has been deleted.',
        html_message=html_content
    )


post_limit = 3


# @receiver(pre_save, sender=Post)
# def postcreate_limit(instance, sender, **kwargs):




