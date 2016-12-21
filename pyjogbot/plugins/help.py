import re
import random

from slackbot.bot import respond_to, default_reply

from pyjogbot import bot

help_dict = {
    "ebook": "PacktPub 에서 매일 무료로 배포하는 EBook 을 확인",
    "육회": "다음 육회먹는 파이조그(10n+6회) 확인"
}


@respond_to('^help$', re.IGNORECASE)
def help(message):
    msg = "[ PyJog EVE Bot 명령어 도움말 ]\n"
    for k, v in help_dict.items():
        msg += "%s : %s\n" % (k, v)
    message.send(msg)


@default_reply
def default_reply(message):
    channel_body = getattr(message.channel, "_body", None)
    if channel_body['name'] != 'bot_test':
        slack_client = getattr(bot, "_client", None)
        channel_id = slack_client.find_channel_by_name('bot_test')
        message.send("봇 테스트는 <#%s|%s> 에서 해주세요" % (channel_id, "bot_test"))
        return

    msg = message.body['text']
    if "주인" in msg:
        message.send("주인님은 건들지 마시죠")
    else:
        message.send("Please input your password")
