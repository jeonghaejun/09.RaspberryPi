from audioapi import *

# 음성 인식
with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()

ret, data = stt(audio)
if ret:
    print(data)
    # 문장 --> 의미를 어떻게 해석할거냐? --> AI 역할...
else:
    print('인식 실패', data)
