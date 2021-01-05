from webapp import create_app
from vk_parser import *
import re


def preprocess_text(text):
    text = text.lower().replace('ё', 'е')
    text = text.replace('d', '')
    text = text.replace('rt', '')
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
    text = re.sub('@[^\s]+', '', text)
    text = re.sub(r'\b[a-zA-Zа-яА-Я1-9]\b', '', text)
    text = re.sub(r'[0-9]', '', text)
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()


app = create_app()
with app.app_context():
    query = Comment.query.all()
    preprop_comm = []

    for comment in query:
        preprop_comm.append(preprocess_text(comment.comment_text))

print(preprop_comm)
