import net
import json

import cv2
import numpy as np

HOST = '192.168.0.4'
PORT = 5000


def show_image(data):
    # byte 배열을 numpy로 변환
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('frame', image)
    cv2.waitKey(1)  # 이미지 갱신이 실제 일어나는 곳.


def receiver(client, addr):

    reader = client.makefile('rb')
    writer = client.makefile('wb')
    while True:
        data, data_len = net.receive(reader)
        if not data:
            break
        # print('received ', data_len)  # 이미지 처리
        # AI 알고리즘 처리 - 불량 여부 판단... 여기에 넣으면됭
        show_image(data)
        result = json.dumps({'result': 'ok'})
        net.send(writer, result.encode())

    print('exit receiver')


if __name__ == '__main__':
    print('start server...')
    net.server(HOST, PORT, receiver)
