from webapp import create_app
from vk_parser import *
import re


def preprocess_text(text):
    text = text.lower().replace("ё", "е")
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'USER', text)
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
