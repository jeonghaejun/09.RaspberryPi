def get_resolution():
    # 해상도를 선택하도록 함
    res = int(input('Resolution(1:320x240, 2:640x480, 3:1024x768)?'))

    # 선택한 값에 따라 해상도 설정
    if res == 3:
        resolution = (1024, 768)
    elif res == 2:
        resolution = (640, 480)
    else:
        resolution = (320, 240)

    return resolution
