from celery import shared_task, shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery ha funcionado!!',
    'ESTO ES UNA PRUBEA DE QUE HA FUNCIONADO!!',
    'josedondis@gmail.com',
    ['jedondis@gmail.com'])


