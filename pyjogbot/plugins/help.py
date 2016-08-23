import re

from slackbot.bot import respond_to

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
