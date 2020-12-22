from webapp import create_app
from vk_parser import *

app = create_app()
with app.app_context():
    take_posts()