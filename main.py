from heater import Heater
from ptc import PTC
from pid import PIDController

from machine import Timer

#Inicializacion 
heater = Heater(16)
ptc = PTC(28)
pid = PIDController(0.6,0.01, 0.001)

setpoint = 5000
pid.setSetpoint(setpoint)

def calculate():
  currTemp = ptc.read()
  output = pid.update(currTemp)
  heater.update(output)
  print("Temperatura: ",currTemp,"\t\tSeteado: ",setpoint,"\t\tControl: ", output)

calculate()
