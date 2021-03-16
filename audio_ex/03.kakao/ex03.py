import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = '9fd6e9e7251cbfb5ee6c2ea8c8a8423e'

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}

with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()

res = requests.post(kakao_speech_url, headers=headers, data=audio)

if res.status_code == 200:  # 성공
    print(res.text)
else:  # 실패
    print(res.status_code)
    print(res.json())

# multipart

# finalResult 를 추출하는 방법

result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]

result = json.loads(result_json_string)
print(result)
print(result['value'])
