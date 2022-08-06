from machine import Pin, PWM                      #include hardware devices
from time import sleep                            #include delay time


class Fan:
    def __init__(self):
        self.pwm = PWM(Pin(7))
        self.pwm.freq(1000)

    def run(self, duty):
        self.pwm.duty_u16(duty)
