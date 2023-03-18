from heater import Heater
from pid import PIDController
from max6675 import MAX6675
from utils import map_value
import time

so = 15
sck = 13
cs = 14

#Inicializacion 
max = MAX6675(sck,cs,so)
heater = Heater(16)
pid = PIDController(25, 2.5 , 0.25)

setpoint = 35

pid.setSetpoint(setpoint)

def calculate():
  currTemp = max.read()
  output = pid.update(currTemp)
  outputScaled = int(map_value(output, -100, 100,-65535,65535))
  outputScaled = 0 if outputScaled < 0 else 65535 if outputScaled > 65535 else outputScaled
  heater.update(outputScaled)
  print("Temperatura: {:.2f} C \tSeteado: {} C \tControl: {:.2f}\tControl Escalado: {}".format(currTemp, setpoint, output, outputScaled))


while True:
  calculate()
  time.sleep_ms(500)
