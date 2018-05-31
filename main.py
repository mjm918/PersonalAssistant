import threading
import voiceAssistant as bot
from localdb import Data
from commands import command as cmd


def commands():
    run = True
    while run:
        cli = raw_input('[>]')
        run = cmd(cli)


def assistant():
    greet = None
    db = Data()
    cursor = db.select('SELECT * FROM greet LIMIT 1 OFFSET ABS(RANDOM()) % MAX((SELECT COUNT(*) FROM greet), 1)')
    for row in cursor:
        greet = row[1]
    bot.speakOut("Hello!! I'm Rapanzel."+greet)
    commnadThread = threading.Thread(target=commands)
    commnadThread.start()
    commnadThread.join()


if __name__ == '__main__':
    assistantThread = threading.Thread(target=assistant)
    assistantThread.start()
    assistantThread.join()