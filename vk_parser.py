import requests
import settings
import time
from datetime import datetime
import csv
from urllib.error import HTTPError
from webapp.models import Post, Group, Comment, db
import sqlite3


def take_posts(group_name):
    all_posts = []
    count = 100
    offset = 0
    VK_POSTS = 'https://api.vk.com/method/wall.get'

    try:
        while offset < 100:
            response = requests.get(VK_POSTS,
                                    params={
                                        'access_token': settings.TOKEN,
                                        'v': settings.API_VERSION,
                                        'domain': str(group_name),
                                        'count': count,
                                        'offset': offset
                                    })
            response.raise_for_status()
            data = response.json()['response']['items']
            offset += count
            all_posts.extend(data)
            time.sleep(0.5)

            for post in all_posts:
                bd_save_posts(group_id=post['from_id'],
                              post_id=post['id'],
                              date=datetime.fromtimestamp(post['date']),
                              text=post['text'],
                              likes=post['likes']['count'])

                take_comments(owner_id=post['from_id'], post_id=post['id'])

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def take_comments(owner_id, post_id):
    all_comments = []
    counts = 1000  # max number of comments
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
        all_comments.extend(data)
        time.sleep(0.5)
        for comment in all_comments:
            bd_save_comments(post_id=comment['post_id'],
                             owner_id=comment['id'],
                             date=datetime.fromtimestamp(comment['date']),
                             comment_text=comment['text'],
                             likes=comment['thread']['count'],
                             sentiment=0)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


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


def posts_ids(posts):
    ids = []
    for post in posts:
        ids.append(post["id"])

    return ids


def bd_save_groups(group_id, domain, group_name):
    group_exists = Group.query.filter(Group.group_id == group_id).count()
    url_exists = Group.query.filter(Group.domain == domain).count()

    group_group = Group(group_id=group_id,
                        domain=domain,
                        group_name=group_name)
    if not (url_exists and group_exists):
        try:
            db.session.add(group_group)
            db.session.commit()
        except sqlite3.IntegrityError as int_err:
            print(f"ooops it is {int_err}")
        finally:
            db.session.close()


def bd_save_posts(group_id, post_id, date, text, likes):
    post_exists = Post.query.filter(Post.post_id == post_id).count()
    group_exists = Post.query.filter(Post.group_id == group_id).count()

    print("posts and groups exists= ",post_exists, group_exists)

    post_post = Post(group_id=group_id,
                     post_id=post_id,
                     date=date,
                     text=text,
                     likes=likes)
    if not (post_exists and group_exists):
        try:
            db.session.add(post_post)
            db.session.commit()
        except sqlite3.IntegrityError as int_err:
            print(f"ooops it is {int_err}")
        finally:
            db.session.close()


def bd_save_comments(post_id, owner_id, date, comment_text, likes, sentiment):

    post_exists = Comment.query.filter(Comment.post_id == post_id).count()
    owner_exists = Comment.query.filter(Comment.owner_id == owner_id).count()

    print('posts and owners exists=',post_exists, owner_exists)

    comm_comm = Comment(post_id=post_id,
                        owner_id=owner_id,
                        date=date,
                        comment_text=comment_text,
                        likes=likes,
                        sentiment=sentiment)

    if not (post_exists and owner_exists):
        try:
            db.session.add(comm_comm)
            db.session.commit()
        except sqlite3.IntegrityError as int_err:
            print(f"ooops it is {int_err}")
        finally:
            db.session.close()
