import subprocess
from localdb import Data
from gtts import gTTS


def speakOut(text):
    isActive = 0
    db = Data()
    cursor = db.select('select * from settings where name = "voice"')

    print(text)

    for row in cursor:
        isActive = row[2]

    if isActive == 1:
        language = "en-us"
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save('tts.mp3')
        subprocess.call(['mpg321', 'tts.mp3', '-quiet'])
        subprocess.call(['rm', 'tts.mp3'])