from machine import Pin, ADC
from math import log


class NTC:
    def __init__(self, pin:int):
        self.adc =  ADC(Pin(pin))
        self.R1 = 98600
        self.c1 = 2.114990448e-03
        self.c2 = 0.3832381228e-04
        self.c3 = 5.228061052e-07
        self.lastR2 = 0


    def read(self) -> float:
            print('\033[2J\033[H')  # ANSI escape code to clear the screen
            reading = self.adc.read_u16()
            print("reading: ", reading)
            voltage=  reading * (3.3/65535.0)
            print("voltage: ", voltage)
            R2 = self.R1 * (3.3/voltage - 1.0)
            R2 = R2 if R2 != 0 else self.lastR2
            self.lastR2 = R2
            print("R2: ", R2)
            logR2 = log(R2)
            print("logR2: ", logR2)
            temp = (1.0 / (self.c1 + self.c2*logR2 + self.c3*logR2*logR2*logR2))
            temp -= 273.15
            print("temp: ", temp)
            print()
            return temp