from audioapi import *
import io
from pydub import AudioSegment
from pydub.playback import play

while True:
    input_str = input("입력: ")
    if input_str == "quit":
        break

    ret, data = tts(input_str)
    if ret:
        sound = io.BytesIO(data)
        song = AudioSegment.from_mp3(sound)
        play(song)
    else:
        print(data)
