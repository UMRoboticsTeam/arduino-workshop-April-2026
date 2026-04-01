#include <Servo.h>

#define BAUD 115200

// Ultrasonic sensor connected to pins 10 and 11
#define TRIGGER_PIN 10
#define ECHO_PIN 11

// Servo connected to pin 3, with the ultrasonic sensor mounted on top of it!
#define SERVO_PWM 3

// Custom timeout for less delay
#define TIMEOUT 10000L

Servo myServo;

void setup() {
  Serial.begin(BAUD);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  myServo.attach(SERVO_PWM);
}

int getDistance() {
    digitalWrite(TRIGGER_PIN, LOW);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, HIGH);

    long pulseLength = pulseIn(ECHO_PIN, HIGH, TIMEOUT);

    int distance = pulseLength*0.034/2;
    return distance;
}

void loop() {
  for (int i = 0; i <= 180; i++) {
    myServo.write(i);

    int distance = getDistance();

    Serial.print(i);
    Serial.print(":");
    Serial.println(distance);
    delay(15);

  }
  myServo.write(0);
  delay(400);
}
