# Мой первый опыт с кроном , также связи с определенным аккаунтом инстаграмма

import requests
from django.conf import settings

from applications.core.models import Image


def my_cron_job():
    url = f'https://graph.instagram.com/me/media?fields=media_type,media_url&access_token={settings.INSTA_API_TOKEN}&limit=20'
    response = requests.get(url).json()
    images = []
    for item in response['data']:
        if len(images) < 9 and item['media_type'] == 'IMAGE':
            images.append(item['media_url'])
    Image.objects.get_or_create(number=1)
    insta = Image.objects.last()
    insta.url = images[0]
    insta.url2 = images[1]
    insta.url3 = images[2]
    insta.url4 = images[3]
    insta.url5 = images[4]
    insta.url6 = images[5]
    insta.url7 = images[6]
    insta.url8 = images[7]
    insta.url9 = images[8]
    insta.save()