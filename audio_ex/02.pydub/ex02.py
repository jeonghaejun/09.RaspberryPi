from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('test.mp3', format="mp3")
# song = AudioSegment.from_mp3('test.mp3')

play(song)