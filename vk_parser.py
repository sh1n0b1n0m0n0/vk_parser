import requests
import settings
import time
import csv


def take_posts(counts):
    all_text = []
    offset = 0
    VK_POSTS = 'https://api.vk.com/method/wall.get'
    try:
        while offset < counts:
            response = requests.get(VK_POSTS,
                                    params={
                                        'access_token': settings.TOKEN,
                                        'v': settings.API_VERSION,
                                        'domain': 'cosy_warhammer',
                                        'count': counts,
                                        'offset': offset
                                    })
            response.raise_for_status()
            data = response.json()['response']['items']
            offset += counts
            all_text.extend(data)
            time.sleep(0.5)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return all_text


def take_comments(owner_id, post_id):
    all_text = []
    counts = 100  # max number of comments
    offset = 0
    VK_COMMENTS = "https://api.vk.com/method/wall.getComments"

    try:
        response = requests.get(VK_COMMENTS,
                                params={
                                    'access_token': settings.TOKEN,
                                    'v': settings.API_VERSION,
                                    'domain': settings.DOMAIN,
                                    'count': counts,
                                    'offset': offset,
                                    'owner_id': owner_id,
                                    'post_id': post_id
                                })

        data = response.json()['response']['items']
        all_text.extend(data)
        time.sleep(0.5)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return all_text


def write_to_text(posts):
    with open('waha.txt', 'a', encoding="utf-8") as file:
        for text in posts:
            str_id = str(text["owner_id"])
            file.write(f'owner_id = {str_id}\n{text["text"]}\n\n##########################################################\n\n')


def write_to_csv(posts):
    with open('wrongart.csv', 'w', encoding="utf-8") as file:
        wr = csv.writer(file, dialect='excel')
        for post in posts:
            wr.writerows(post['text'])


posts = take_posts(10)
owner_id = posts[0]["owner_id"]

print(take_comments(owner_id, 168327))
