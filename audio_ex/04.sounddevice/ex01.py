import sounddevice as sd

duration = 5.5  # seconds


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    # indata를 가지고 여러가지 사운드 처리 할 수 있음.
    outdata[:] = indata


with sd.Stream(channels=1, callback=callback):
    sd.sleep(int(duration * 1000))
