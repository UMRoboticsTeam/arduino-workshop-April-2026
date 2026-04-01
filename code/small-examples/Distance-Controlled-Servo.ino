#include <Servo.h>

#define BAUD 115200

// Ultrasonic sensor connected to pins 10 and 11
#define TRIGGER_PIN 10
#define ECHO_PIN 11

// Servo connected to pin 3
#define SERVO_PWM 3

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

    long pulseLength = pulseIn(ECHO_PIN, HIGH);

    int distance = pulseLength*0.034/2;
    return distance;
}

void loop() {
  int distance = getDistance();
  Serial.println(distance);
  myServo.write(distance);
  delay(100);
}
