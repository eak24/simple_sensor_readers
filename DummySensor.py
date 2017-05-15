import os
import binascii
import random
import sensor_manager

def get_sensor_readings():
	sensors = []
	nSensors = 16
	for i in range(nSensors):
		sensors.append(sensor_manager.SensorReadingClass(random.randint(0,100), "Celsius", binascii.b2a_hex(os.urandom(15))))
	return sensors