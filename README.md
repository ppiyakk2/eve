# PyJog Slack Bot 'EVE'
'EVE' 는 PyJog Slack 에 서식하는 로봇입니다.
'EVE' 라는 이름은 영화 WELL-E 에 나오는 캐릭터에서 가져왔습니다.
 
PyJog 에 대해서 알고 싶으시다면, [여기](https://www.facebook.com/pyjog) 에서 확인해주세요. !!!
 
 
## 개발 환경
Python 3.5
 
 
## 실행 하기
봇을 실행하기 전, [PyJog slack app](https://pyjog.slack.com/apps) 에서 발급받은 API_KEY 를 slackbot_settings.py 에 넣어주세요.

```
# virtualenv 생성
virtualenv -p python3 venv
source venv/bin/activate

# 의존 라이브러리 설치
pip install -r requirements.txt

# 봇 실행
python bot.py
```

## 개발하기
EVE는 [https://github.com/lins05/slackbot](https://github.com/lins05/slackbot) 를 이용해서 만들었습니다.
lins05/slackbot 에서 설명하는 개발 방법을 참고해서 기능을 추가해주시면 됩니다.
새로운 기능을 추가하셨다면, pull request 를 보내주세요!!
 
### PEP8 검사
코드 컨벤션을 유지하기 위해, pep8 을 준수합니다. commit 전, 아래 명령어로 코드 검사를 진행해주세요.
```
make flake
```
