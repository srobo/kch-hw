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
    #HEARTBEAT = 19

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

    @classmethod
    def rows(cls):
        return [
            (cls.BOOT_20, cls.BOOT_40, cls.BOOT_60, cls.BOOT_80, cls.BOOT_100),
            (cls.CODE, cls.COMP),
            (cls.WIFI),  #cls.HEARTBEAT
            (cls.START, cls.STATUS_RED, cls.STATUS_GREEN, cls.STATUS_BLUE),
            (
                cls.USER_A_RED, cls.USER_A_GREEN, cls.USER_A_BLUE,
                cls.USER_B_RED, cls.USER_B_GREEN, cls.USER_B_BLUE,
                cls.USER_C_RED, cls.USER_C_GREEN, cls.USER_C_BLUE
            )
        ]


GPIO.setmode(GPIO.BCM)

try:
    GPIO.setup(LEDs.all(), GPIO.OUT, initial=GPIO.LOW)

    while True:
        # All
        GPIO.output(LEDs.all(), GPIO.HIGH)
        sleep(2)
        GPIO.output(LEDs.all(), GPIO.LOW)
        sleep(1)

        # Rows
        for row in LEDs.rows():
            GPIO.output(row, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(row, GPIO.LOW)

        sleep(1)

        # Chase
        for led in LEDs:
            GPIO.output(led, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led, GPIO.LOW)

        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
