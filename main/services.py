import stripe
from config import settings
import requests
from main.models import Payment


def checkout_session(course, user):
    headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}
    data = [
        ('amount', course.price),
        ('currency', 'usd'),
    ]
    response = requests.post('https://api.stripe.com/v1/payment_intents', headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f'ошибка : {response.json()["error"]["message"]}')
    return response.json()


def create_payment(course, user):
    Payment.objects.create(
        user=user,
        payed_course=course,
        sum_payed=course.price,
    )
