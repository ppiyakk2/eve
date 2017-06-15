import json
import os
import re
from datetime import datetime

import requests
from slackbot.bot import respond_to

from pyjogbot import bot, sched
from slackbot_settings import ROOT_DIR, FACEBOOK_APP_TOKEN

URL = 'https://graph.facebook.com/{}'
FILE_PATH = os.path.join(ROOT_DIR, 'event_history.json')
DATETIME_FORMAT = "%Y년 %m월 %d일 %H시 %M분"


def get_event_history():
    try:
        with open(FILE_PATH, 'r') as f:
            data = f.read()
            data = json.loads(data)
            return data
    except FileNotFoundError:
        data = {'events': []}
        set_event_history(data)
        return data


def set_event_history(data):
    with open(FILE_PATH, 'w') as f:
        f.write(json.dumps(data))
    return


def get_event(page):
    params = {'access_token': FACEBOOK_APP_TOKEN, 'fields': 'events'}
    graph_result = requests.get(URL.format(page), params=params)
    if graph_result.status_code == 200:
        return graph_result.json()
    else:
        return None


def get_recent_pyjog_event():
    params = {'access_token': FACEBOOK_APP_TOKEN, 'fields': 'events'}
    graph_result = requests.get(URL.format('pyjog'), params=params)
    if graph_result.status_code == 200:
        events = graph_result.json()
    else:
        return None
    recent_event = events['events']['data'][0]
    pyjog_event_day = datetime.strptime(
        recent_event['start_time'],
        '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=None)
    recent_event['pyjog_event_day'] = pyjog_event_day
    return recent_event


def make_event_message(event):
    message = u'*{} {}*'.format(
        event['name'],
        event['pyjog_event_day'].strftime(DATETIME_FORMAT)
    )
    location = ('{description}\n\n'
                '위치: {location}\n'
                '지도보기: http://maps.google.com/maps?q={location}\n'
                '페이스북 이벤트: http://www.facebook.com/events/{id}'
                .format(location=event['place']['name'], id=event['id'],
                        description=event['description']))
    attachments = json.dumps([
        {
            'color': '#48D0FF',
            'fields': [
                {
                    'value': location,
                    'short': False
                }
            ],
            'mrkdwn_in': ['text', 'fields']
        }
    ])
    return message, attachments


@sched.scheduled_job('cron', hour=10)
def pyjog_event_notify():
    event = get_recent_pyjog_event()
    if event is None or event['pyjog_event_day'] < datetime.now():
        return
    event_history = get_event_history()
    if event['id'] in event_history['events']:
        return

    event_history['events'].append(event['id'])
    set_event_history(event_history)
    slack_client = getattr(bot, "_client", None)
    channel_id = slack_client.find_channel_by_name('general')
    message, attachments = make_event_message(event)
    slack_client.send_message(channel_id, message, attachments)


@respond_to('^파이조그$|^pyjog$', re.IGNORECASE)
def pyjog_event_ask(message):

    event = get_recent_pyjog_event()

    if event is None or event['pyjog_event_day'] < datetime.now():
        last_event_time = (event['pyjog_event_day'].strftime(DATETIME_FORMAT))
        comment = ("아직 다음 파이조그 이벤트가 만들어지지 않았어요.\n"
                   "마지막 파이조그 이벤트는 {name} {last_event_time} 이었습니다."
                   .format(name=event['name'],
                           last_event_time=last_event_time))
        message.send(comment)
    else:
        comment, attachments = make_event_message(event)
        message.send_webapi("다음 파이조그 정보입니다.\n{}".format(comment),
                            attachments)
