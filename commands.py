import voiceAssistant as bot
from localdb import Data
import datetime as dt

keys = ['time', 'addtask', 'showtask', 'modifytask', 'today', 'manual', 'addlink', 'links', 'modifylink', 'open', 'close', 'mute', 'unmute', 'exit', 'setting']


def command(cmd):
    cmd = str(cmd).strip()
    if "exit" not in cmd:
        valid = check_command(cmd)
        if valid:
           return execute_command(cmd)
        return True
    else:
        bot.speakOut("Alright! Have a nice day")
        return False


def execute_command(cmd):
    db = Data()
    db_result = -2
    keywords = str(cmd).split(" ")
    keyword = keywords[0]
    if keyword == "setting":
        db_result = db.insert("insert or replace into settings (name, val) VALUES ('"+keywords[1]+"',"+keywords[2]+")")
        bot.speakOut("Setting has been set successfully") if db_result == 1 else bot.speakOut("Something went wrong")
    elif keyword == "mute":
        db_result = db.insert("insert or replace into settings (name, val) VALUES ('voice',0)")
        bot.speakOut("Voice assistant has been inactivated") if db_result == 1 else bot.speakOut("Something went wrong")
    elif keyword == "unmute":
        db_result = db.insert("insert or replace into settings (name, val) VALUES ('voice',1)")
        bot.speakOut("Voice assistant has been activated") if db_result == 1 else bot.speakOut("Something went wrong")
    elif keyword == "time":
        now = dt.datetime.now()
        strdate = dt.date(day=now.day, month=now.month, year=now.year).strftime('%A %d %B %Y')
        bot.speakOut("Today is "+strdate+" and the time is "+str(display_time(dt.datetime.now().strftime('%I %M %H'))))

    return True


def check_command(cmd):
    keywords = str(cmd).split(" ")
    keyword = keywords[0]
    if keyword not in keys:
        bot.speakOut('Command not found. Type `manual` to see all the available commands')
        return False
    else:
        return validate_command(cmd)


def validate_command(cmd):
    split = str(cmd).split(" ")
    if split[0] == "setting" and len(split) != 3:
        bot.speakOut("Invalid command. Three arguments expected")
        return False
    elif split[0] == "time" and len(split) > 1:
        bot.speakOut("Invalid command. No argument expected")
        return False
    else:
        return True


d = {0: "(oh)",
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
     10: "ten",
     11: "eleven",
     12: "twelve",
     13: "thirteen",
     14: "fourteen",
     15: "fifteen",
     16: "sixteen",
     17: "seventeen",
     18: "eighteen",
     19: "nineteen",
     20: "twenty",
     30: "thirty",
     40: "forty",
     50: "fifty",
     60: "sixty"}


def display_time(t):
    Hour = d[int( t[0:2])] if t[0:2] != "00" else d[12]
    Suffix = 'a.m' if d[int( t[7:9])] == Hour else 'p.m'

    if  t[3] == "0":
        if  t[4] == "0":
            Minute = ""
        else:
            Minute = d[0] + " " + d[int(t[4])]
    else:
        Minute = d[int(t[3])*10] + '-' + d[int(t[4])]
    return Hour+" "+Minute+" "+Suffix
