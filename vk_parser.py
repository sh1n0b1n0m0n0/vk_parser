import requests
import settings
import time
import csv


def take_10_posts():
    all_posts = []
    count = 10
    offset = 0

    while offset < 10:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': settings.TOKEN,
                                    'v': settings.API_VERSION,
                                    'domain': settings.DOMAIN,
                                    'count': count,
                                    'offset': offset
                                })

        data = response.json()['response']['items']
        offset += 10
        all_posts.extend(data)
        time.sleep(0.5)

    return all_posts


def write_to_text(posts):
    with open('wrongart.txt', 'a', encoding="utf-8") as file:
        for text in posts:
            file.write(text['text'])


def write_to_csv(posts):
    with open('wrongart.csv', 'w', encoding="utf-8") as file:
        wr = csv.writer(file, dialect='excel')
        for post in posts:
            wr.writerows(post['text'])


posts = take_10_posts()
write_to_text(posts)
write_to_csv(posts)

