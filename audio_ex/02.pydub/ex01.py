from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('test.wav', format="wav")
# song = AudioSegment.from_wav('test.wav')

play(song) # 동기 함수인가? 비동기 함수인가? 답 동기함수
print("exit")