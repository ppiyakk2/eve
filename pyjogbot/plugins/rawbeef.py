import re
from slackbot.bot import respond_to
import datetime


def calc_next_rawbeef():
    next_rawbeef = datetime.date(2016, 9, 3)
    next_count = 46
    today = datetime.date.today()

    while today >= next_rawbeef:
        last_rawbeef = next_rawbeef
        last_count = next_count
        next_rawbeef = last_rawbeef + datetime.timedelta(weeks=20)
        next_count = last_count + 10

    return next_rawbeef, next_count


@respond_to('육회', re.IGNORECASE)
def next_rawbeef(message):
    next = calc_next_rawbeef()
    message.send("다음 육회조그(%d회)는 별다른 일이 없다면 %s년 %s월 %s일 입니다(D-%d)."\
		 % (next[1], next[0].year, next[0].month, next[0].day, (next[0]-datetime.date.today()).days))

