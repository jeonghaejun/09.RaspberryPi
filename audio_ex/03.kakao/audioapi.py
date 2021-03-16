# 음성 인식/합성을 위한 helper 함수 제작

# 음성 합성 함수명 stt()
# 매개변수: 합성할 문자열, 음색(디폴트값 지정)
# 반환값: 성공여부, mp3 데이터(실패시 이유)

# 음성 인식 함수명 stt()
# 매개변수 : 음성 데이터(BytesIO 객체)
# 반환값: 성공여부, 인식 문자열


import requests
import io
import json

API_KEY = '9fd6e9e7251cbfb5ee6c2ea8c8a8423e'
TTS_URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
TTS_HEADERS={
    "Content-Type":"application/xml",
    "Authorization":"KakaoAK "+ API_KEY
}

STT_URL = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
STT_HEADERS={
    "Content-Type":"application/OCTET-STREAM",
    "X-DSS-Service": "DICTATION",
    "Authorization":"KakaoAK "+ API_KEY
}


def tts(input_str, voice="WOMAN_DIALOG_BRIGHT"):
    
    xml=f'<speak><voice name="MAN_DIALOG_BRIGHT">{input_str}</voice></speak>'
    res=requests.post(TTS_URL,headers=TTS_HEADERS,data=xml.encode('utf-8'))

    if res.status_code==200:
        return True,res.content
    else:
        return False,res.json()


def stt(audio):
    res=requests.post(STT_URL,headers=STT_HEADERS,data=audio)
    if res.status_code==200:
        result_json_string=res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        result=json.loads(result_json_string)
        return True, result['value']
    else:
        return False,res.json()
