# mp3 -> wav
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file('test.mp3', format="mp3")
sound.export('converted.wav', format="wav")
