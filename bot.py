import signal

import pyjogbot


def sigterm(signum, frame):
    pyjogbot.sched.shutdown()


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm)
    signal.signal(signal.SIGINT, sigterm)

    pyjogbot.sched.start()
    pyjogbot.bot.run()
