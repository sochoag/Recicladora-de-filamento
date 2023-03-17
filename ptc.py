from machine import Pin, ADC

class PTC:
    def __init__(self, pin:int):
        self.adc =  ADC(Pin(pin))

    def read(self):
            return self.adc.read_u16()