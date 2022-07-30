#!/usr/bin/env python3
from time import sleep
from enum import IntEnum, unique

import RPi.GPIO as GPIO


@unique
class LEDs(IntEnum):
    BOOT_20 = 7
    BOOT_40 = 5
    BOOT_60 = 12
    BOOT_80 = 6
    BOOT_100 = 13

    CODE = 11
    COMP = 16

    WIFI = 8
    HEARTBEAT = 19

    START = 9
    STATUS_RED = 26
    STATUS_GREEN = 20
    STATUS_BLUE = 21

    USER_A_RED = 24
    USER_A_GREEN = 10
    USER_A_BLUE = 25
    USER_B_RED = 27
    USER_B_GREEN = 23
    USER_B_BLUE = 22
    USER_C_RED = 4
    USER_C_GREEN = 18
    USER_C_BLUE = 17

    @classmethod
    def all(cls):
        return list(map(lambda c: c.value, cls))


GPIO.setmode(GPIO.BCM)

try:
    GPIO.setup(LEDs.all(), GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(LEDs.BOOT_20, GPIO.HIGH)
    sleep(1)

    # Chase
    for led in LEDs:
        GPIO.output(led, GPIO.HIGH)
        sleep(0.25)
        GPIO.output(led, GPIO.LOW)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
