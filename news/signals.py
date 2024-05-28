from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.template.loader import render_to_string
from project.settings import SITE_URL
from project import settings

from .models import Category


def send_notification(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/{pk}'
        }
        )

    msg = EmailMultiAlternatives(
        subject=title,  
        body='',  
        from_email=settings.DEFAULT_FROM_EMAIL,  
        to=subscribers
    )

    msg.attach_alternative(html_content,  "text/html")
    msg.send()


@receiver(m2m_changed, sender=Category)
def Post_created(instance, created, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers = list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()


        subscribers = [s.email for s in subscribers]

        send_notification(instance.preview(), instance.pk, instance.title, subscribers)
    # if not created:
    #     return

    # emails = User.objects.filter(
    #     subscriptions__category=instance.category
    # ).values_list('email', flat=True)

    # subject = f'Новый пост в категории {instance.category} !'

    # text_content = (
    #     f'Название: {instance.title}\n'
    #     f'Дата: {instance.datetime}\n\n'
    #     f'Перейти...: http://127.0.0.1:8000{instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Название: {instance.title}<br>'
    #     f'Дата: {instance.datetime}<br><br>'
    #     f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
    #     f'Перейти...</a>'
    # )
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()