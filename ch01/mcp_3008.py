import spidev
import time

delay = 0.5

pot_channel = 0

spi = spidev.SpiDev()

spi.open(0, 0)

spi.max_speed_hz = 100000

# 0 ~7 까지 8개의 채널에서 SPI 데이터 읽기
def readadc(adcnum):
    if adcnum < 0 or adcnum > 7:
        return -1

    r = spi.xfer2([1, 8+adcnum <<4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    
    return data

while True:
# readadc 함수로 pot_channel의 SPI 데이터를 읽기
    pot_value = readadc(pot_channel)
    print("---------------------------")
    print("POT value: %d" % pot_value)
    time.sleep(delay)
