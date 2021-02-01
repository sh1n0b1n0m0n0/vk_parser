from webapp import create_app
from vk_parser import *

app = create_app()
group_name = 'pesbl'#'warhammer_art_of_war'
with app.app_context():
    take_groups(group_name)
    take_posts(group_name)
