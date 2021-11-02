from django.contrib.auth import get_user_model
from celery import shared_task
from CeleryDjango import settings
from django.core.mail import message, send_mail

User = get_user_model()

@shared_task(bind=True)
def test_func(self):
    return "Hello"


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Hi! This is my Second Mail"
        message = "This mail is used for testing purpose"
        to_email = user.email

        send_mail(
            subject=mail_subject,
            message=message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_email], 
            fail_silently = True
            )
    return "Done"