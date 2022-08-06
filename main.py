from time import sleep_ms
import time
import machine
from machine import I2C, Pin
from lcd1602_i2c import I2cLcd
from lcd1602_i2c import DEFAULT_I2C_ADDR
from steering import Steering_Engine
from PIR import PIR_Sensor
from laser import Laser
from fan import Fan


if __name__ == "__main__":
    # settings
    repeat_times = 5
    repeat_delay = 900    # seconds delayed until the next session
    repeat_fan = 5
    play_enabled = True

    # initialize moduls
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)               #define LCD I/O PIN and Freq.
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)                     #define I2C defult address.
    lcd.show_welcome()

    laser = Laser()
    fan = Fan()
    se = Steering_Engine()
    pir = PIR_Sensor()

    while(True):
        if play_enabled == True:

            pir_value = pir.read_value()
            # Cat or Human detected
            if pir_value:
                sleep_ms(5000)
                for i_repeat in range(repeat_times):
                    # Cat chasing the laser-pointer
                    laser.laser_on()
                    se.stear()

                    sleep_ms(5000)

                    # Cat chasing the spinning feather attached to the fan            
                    for i_duty in range(repeat_fan):
                        for duty in range(0, 30000, 100):
                            fan.run(duty)    # 0 to max. 65000
                        sleep_ms(5000)

                        for duty in range(30000, 0, -100):
                            fan.run(duty)    # 0 to max. 65000
                        sleep_ms(5000)
                            
                    laser.laser_off()

                play_enabled = False
                time_last_played = time.time()

        
        else:
            time_diff = time.time() - time_last_played
            lcd.clear()
            lcd.move_to(1, 0)
            lcd.putstr("Play-Time in:")
            lcd.move_to(1, 1)
            lcd.putstr(str(repeat_delay-time_diff)+" seconds")
            sleep_ms(1000)
            lcd.clear()

            if (time_diff > repeat_delay):
                play_enabled = True

