import machine                                                       #include hardware devices
import utime                                                         #include delay time


class Laser:
    def __init__(self):
        self.led_laser = machine.Pin(6, machine.Pin.OUT)                      #define LED pin function:GP15,ouput function

    def laser_on(self):
        self.led_laser.value(1)

    def laser_off(self):
        self.led_laser.value(0)