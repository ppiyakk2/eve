import re

from slackbot.bot import respond_to

help_dict = {
    "ebook": "PacktPub 에서 매일 무료로 배포하는 EBook 을 확인"
}


@respond_to('help', re.IGNORECASE)
def help(message):
    msg = "[ PyJog EVE Bot 도움말 ]"
    for k, v in help_dict.items():
        msg += ""
