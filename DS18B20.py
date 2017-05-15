from w1thermsensor import W1ThermSensor
import sensor_manager

# for sensor in W1ThermSensor.get_available_sensors():
#     print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

def get_sensor_ids():
	return [sensor.id for sensor in W1thermsensor.get_available_sensors]

def get_sensor_value(sensor_id):
	return [sensor.get_temperature for sensor in W1thermsensor.get_available_sensors if sensor.id == sensor_id]

def get_sensor_readings():
	sensors = []
	for sensor in W1ThermSensor.get_available_sensors():
		sensors.append(sensor_manager.SensorReadingClass(sensor.get_temperature(), "Celsius", sensor.id))
	return sensors
