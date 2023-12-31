from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta
from config import settings
from main.models import SubscriptionCourse
from users.models import User


@shared_task
def send_updated_email(course):
    subscribers_list = SubscriptionCourse.objects.filter(course=course)
    for sub in subscribers_list:
        print('Отправлено сообщение об обновление')
        send_mail(
            'ALARM!',
            f'Сообщаем, что курс на который вы подписаны  обновлён',
            settings.EMAIL_HOST_USER,
            [sub.user]
        )

@shared_task
def check_user():

    now_date = datetime.now()
    one_month_ago = now_date - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)
    inactive_users.update(is_active=False)
    print(inactive_users)