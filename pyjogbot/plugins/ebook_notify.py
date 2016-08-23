import re

import requests
from bs4 import BeautifulSoup as Soup
from slackbot.bot import respond_to

from pyjogbot import bot, sched

url = "https://www.packtpub.com/packt/offers/free-learning"


def get_today_ebook_title():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    if r.status_code != 200:
        return 'error'

    soup = Soup(r.text, 'html.parser')
    dv = soup.find("div", {"class": "dotd-title"})
    title = dv.text.rstrip().lstrip()
    return title


@sched.scheduled_job('cron', hour=9, minute=30)
def notify_to_general_freebook():
    title = get_today_ebook_title()
    slack_client = getattr(bot, "_client", None)
    channel_id = slack_client.find_channel_by_name('bot_test')
    slack_client.send_message(channel_id, "[ 오늘의 무료 EBook ]\n%s\n%s"
                              % (title, url))


@respond_to('^ebook$', re.IGNORECASE)
def today_free_ebook(message):
    title = get_today_ebook_title()
    message.send("[ 오늘의 무료 EBook ]\n"
                 "%s\n%s" % (title, url))
