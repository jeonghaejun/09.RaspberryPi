import picamera
from time import sleep
import socket
import io
import json
import net
HOST = '192.168.0.4'
PORT = 5000

if __name__ == '__main__':
    with socket.socket() as s:
        s.connect((HOST, PORT))
        writer = s.makefile('wb')
        reader = s.makefile('rb')

        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.vflip = True
            stream = io.BytesIO()  # 메모리 파일 스트림
            # JPG 이미지 바로 얻기
            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                image = stream.getvalue()  # 스트림에서 byte 배열 얻기
                # 이미지 전송
                net.send(writer, image)
                result = net.receive(reader)[0]

                # 다음 캡처를 위해 스트림을 리셋 - 파일의 기존 내용을 버림
                stream.seek(0)  # 파일 쓰기 위치를 맨 앞으로 이동
                stream.truncate()  # 기존 내용을 버리는 작업
