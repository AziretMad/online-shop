from huey.contrib.djhuey import task
from django.conf import settings
from django.core.mail import send_mail


@task()
def send_email_account_activation(recipient_email: str, message: str) -> int:
    send_mail(
        "Активация аккаунта",
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email]
    )


@task()
def send_email_password_reset(recipient_email: str, message: str) -> int:
    send_mail(
        "Сброс пароля",
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email]
    )
