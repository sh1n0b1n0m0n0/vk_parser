import requests
import settings

response = requests.get('https://api.vk.com/method/wall.get',
                       params={
                           'access_token': settings.TOKEN,
                           'v': settings.API_VERSION,
                           'domain': settings.DOMAIN
                       })

data = response.json()['response']['items']
for text in data:
    print(text['text'])