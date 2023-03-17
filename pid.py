import time

class PIDController:
  def __init__(self, Kp, Kd, Ki):
    self.Kp = Kp
    self.Ki = Ki
    self.Kd = Kd
    self.lastTime = time.ticks_us()
    self.lastError = 0
    self.integral = 0

  def setSetpoint(self, setpoint):
    self.setpoint = setpoint
  
  def update(self, measured_value):
		# Obtiene el tiempo actual de ejecucion
    currentTime = time.ticks_us()

		# # Calcula el tiempo desde la ultima ejecución
    dt = time.ticks_diff(currentTime, self.lastTime) / 1e6

    # # Calcula el error
    error = self.setpoint - measured_value

    # # Calcula derivativo
    derivative = (error - self.lastError) / dt

    # # Calcula integral
    self.integral += error * dt

    # # Calcula la salida
    output =  self.Kp*error + self.Ki*self.integral + self.Kd*derivative

    # # Actualiza el ultimo tiempo y el ultimo error
    self.lastTime =  currentTime
    self.lastError = error
    return output
