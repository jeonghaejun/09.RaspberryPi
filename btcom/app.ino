// 1. Joystick의 값을 읽어서 LCD에 출력
// 2. Bluetooth로 x, y값을 라즈베리파이에 전송

// Joystick 값으로 무엇을 조정할 거냐?
// 예1: 카메라
// - 서보모터 + 카메라
// - Joystick의 값 --> 서보모터의 회전각
// - button의미? --> 촬영

#include <BtMiniCom.h>
#include <Button.h>
#include <ArduinoJson.h>

void receive(String msg)
{
}

int jX = A0;
int jY = A1;
Button btn(2); // interrupt방식 (2,3번 핀) 이용 예정

BtMiniCom com(12, 13, receive);

void check()
{
    int x = analogRead(jX); // 좌우 조정 의미
    int y = analogRead(jY); // 상하 조정 의미
    // 0 ~ 1023 사이의 값 --> -90 ~ 90
    x = map(x, 0, 1023, -90, 90);
    y = map(y, 0, 1023, -90, 90);
    com.print_i(0, "x: ", x);
    com.print_i(1, "y: ", y);

    // 블루투스로 전송...
    String msg;
    // json 문자열로 전송..
    StaticJsonDocument<128> doc;
    doc["target"] = "servo";
    doc["x"] = x;
    doc["y"] = y;
    serializeJson(doc, msg);
    // Serial.println(msg);
    com.send(msg);
}

void capture()
{
    // if (!btn.debounce()) return;
    String msg;
    StaticJsonDocument<128> doc;
    doc["target"] = "camera";
    doc["camera"] = "capture";
    serializeJson(doc, msg);
    // Serial.println(msg);
    com.send(msg);
}

void setup()
{
    com.init();
    com.setInterval(100, check);
    // 인터랩트 방식을 사용하면 전송 중간에 콜백 함수가 실행될 수 있음.
    // btn.attachInterrupt(capture, FALLING);
    // 폴링 방식으로 변경
    btn.setCallback(capture);
}

void loop()
{
    com.run();
    btn.check(); // 폴링 방식으로 버튼 체크
}
