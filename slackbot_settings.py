import os

#API_TOKEN = ""
#FACEBOOK_APP_TOKEN = ''

DEFAULT_REPLY = "봇 테스트는 #bot_test 에서 해주세요"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PLUGINS = [
    'pyjogbot.plugins.help',
    'pyjogbot.plugins.ebook_notify',
    'pyjogbot.plugins.rawbeef',
    'pyjogbot.plugins.pyjog_event'
]
