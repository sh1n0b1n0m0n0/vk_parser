from webapp import create_app
from vk_parser import *

app = create_app()
group_name = 'warhammer_art_of_war'
with app.app_context():
    take_posts(group_name)