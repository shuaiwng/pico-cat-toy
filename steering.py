from machine import Pin, PWM, Timer
import time
import random


class Steering_Engine():
    def __init__(self):
        self.pwm = PWM(Pin(2))
        #moto run range:500--2500 us,  precision: 0.09°/1us
        #us= duty*20000/65535
        #duyt=us*65535/20000
        self.pwm.freq(50)                               #50hz=20000us duty times=20000/65535
        self.DUTY0 = 1638                               #us= 500us,0°
        self.DUTY20 = 2366                            
        self.DUTY45 = 3276                              #us= 1000us,45°
        self.DUTY70 = 4186
        self.DUTY90 = 4915                              #us= 1500us,90°


    def stear(self):
        self.pwm.duty_u16(self.DUTY0)
        time.sleep(random.randint(1, 2))
        self.pwm.duty_u16(self.DUTY20)
        time.sleep(random.randint(1, 2))
        self.pwm.duty_u16(self.DUTY45)
        time.sleep(random.randint(1, 2))
        self.pwm.duty_u16(self.DUTY70)
        time.sleep(random.randint(1, 2))
        self.pwm.duty_u16(self.DUTY90)


