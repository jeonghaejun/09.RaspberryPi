import pyaudio
import wave

MIC_DEVICE_ID = 1

CHUNK = 1024   # 버퍼 크기
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 16000

RECORD_SECONDS = 5

p = pyaudio.PyAudio()
mic = p.open(input_device_index=MIC_DEVICE_ID,
             format=FORMAT,
             channels=CHANNELS,
             rate=RATE,
             input=True,
             frames_per_buffer=CHUNK)

out = p.open(format=FORMAT,
             channels=CHANNELS,
             rate=RATE,
             output=True)

print("Start to record the audio.")

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    data = mic.read(CHUNK)
    out.write(data)

print("Recording is finished.")

mic.stop_stream()
out.stop_stream()
mic.close()
out.close()
p.terminate()
