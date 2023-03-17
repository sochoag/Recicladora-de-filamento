from machine import Pin, PWM

class Heater:
    def __init__(self, pin:int):
        self.frequency = 1000
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(self.frequency)

    def update(self,newVal:int):
        if(newVal > 65535):
            newVal = 65535
        elif(newVal < 0):
            newVal = 0
        self.pwm.duty_u16(newVal)