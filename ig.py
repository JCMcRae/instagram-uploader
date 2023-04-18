import json
import os
import sys
import webbrowser

import dotenv
import requests
from crontab import CronTab
from dotenv import load_dotenv, find_dotenv

sys.path.insert(0, '')

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

INSTAGRAM_PAGE_ID = os.getenv('INSTAGRAM_PAGE_ID')
GRPAH_API_TOKEN = os.getenv('GRPAH_API_TOKEN')
LONG_LIVED_API_TOKEN = os.getenv('LONG_LIVED_API_TOKEN')
APP_ID = os.getenv('APP_ID')
APP_SECRET = os.getenv('APP_SECRET')
FACEBOOK_ACCESS_TOKEN_URL = os.getenv('FACEBOOK_ACCESS_TOKEN_URL')
GRANT_TYPE = os.getenv('GRANT_TYPE')
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')

def create_instagram_post():
    CAPTION = 'This is a test post.'

    image_location = 'your/image/URL'
    post_url = 'https://graph.facebook.com/v14.0/{}/media'.format(INSTAGRAM_PAGE_ID)

    payload = {
        'image_url': image_location,
        'caption': CAPTION,
        'access_token': GRPAH_API_TOKEN
    }
    r = requests.post(post_url, data=payload)
    print(r.text)

    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']

        second_url = 'https://graph.facebook.com/v14.0/{}/media_publish'.format(INSTAGRAM_PAGE_ID)
        second_payload = {
            'creation_id': creation_id,
            'access_token': GRPAH_API_TOKEN
        }
        r = requests.post(second_url, data=second_payload)

        print('--------Successfully posted test post to IG--------')
        print(r.text)


    else:
        print('Test post unsuccessful. Please see log for errors.')
        

def create_carousel(image_locations, caption):
    post_url = 'https://graph.facebook.com/v14.0/{}/media'.format(INSTAGRAM_PAGE_ID)
    media_publish_url = 'https://graph.facebook.com/v14.0/{}/media_publish'.format(INSTAGRAM_PAGE_ID)

    carousel_post_ids = []

    for image_location in image_locations:
        payload = {
            'image_url': image_location[0],
            'is_carousel_item': True,
            'access_token': GRPAH_API_TOKEN
        }

        request = requests.post(post_url, params=payload)
        container_id = request.json()['id']
        print(f"Successful carousel item created: {container_id}")
        carousel_post_ids.append(container_id)
        print(len(carousel_post_ids))

    carousel_payload = {
        'media_type': 'CAROUSEL',
        'caption': caption,
        'children': carousel_post_ids,
        'access_token': GRPAH_API_TOKEN
    }

    carousel_request = requests.post(post_url, json=carousel_payload)
    print(carousel_request.content)
    creation_id = carousel_request.json()['id']

    publish_payload = {
        'creation_id': creation_id,
        'access_token': GRPAH_API_TOKEN
    }

    publish_id = requests.post(media_publish_url, params=publish_payload)
    print(f"Successful posting of carousel item: {publish_id}")
