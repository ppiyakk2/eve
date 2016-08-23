import datetime
import re

from slackbot.bot import respond_to


def calc_next_rawbeef():
    next_date = datetime.date(2016, 9, 3)
    next_count = 46
    today = datetime.date.today()
    while today >= next_date:
        next_date += datetime.timedelta(weeks=20)
        next_count += 10

    return next_date, next_count


@respond_to('육회', re.IGNORECASE)
def next_rawbeef(message):
    ret = calc_next_rawbeef()
    message.send("다음 육회조그(%d회)는 별다른 일이 없다면 "
                 "%s년 %s월 %s일 입니다(D-%d)."
                 % (ret[1], ret[0].year, ret[0].month, ret[0].day,
                    (ret[0] - datetime.date.today()).days))
