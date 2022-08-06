import machine


# Movement detection
class PIR_Sensor:
    def __init__(self):
        self.aout = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

    def read_value(self):
        return self.aout.value()