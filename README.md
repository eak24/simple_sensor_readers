# simple_sensor_readers

What is this?
A growing collection of small scripts for all types of sensors connected. If you have a new sensor script, please add and make a pull request!

What's in a new sensor script?
A sensor script has four functions: 
	* get_sensor_value(sensor_id), which takes in a string with the serial number, or however get_sensor_ids() returns the sensor ids and it returns the value collected at the sensor.
	* get_sensor_ids(), which returns all the ids of the sensors whose data can be acquired by using this script (for example, if running multiple DS18B20s on one pi)
	* get_units(), which should return a string of signifying the type of units that the sensor senses.
	