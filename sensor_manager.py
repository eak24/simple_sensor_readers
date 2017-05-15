import time
import os


# Test if this is running on the pi. If it is, use the actual sensors, otherwise use dummy sensors. 
# If you want to force this to use dummy sensors, you can force dummy sensors by changing is_pi to true
is_pi = os.uname()[4].startswith("arm")

if is_pi:
	import DS18B20
else: 
	import DummySensor 

def get_sensor_readings():
	sensors = []
	if is_pi:
		sensors= sensors + DS18B20.get_sensor_readings()
	else: sensors = DummySensor.get_sensor_readings()
	return sensors

class SensorReadingClass:
	"""A simple class for any sensor reading. The goal is to standardize how the sensor readings are represented"""
	def __init__(self, data, units, id, time=time.time()):
		self.data = data
		self.units = units
		self.id = id
		self.time = time
