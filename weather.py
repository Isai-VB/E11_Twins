import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
	current_time = time.strftime("%H:%M:%S", t)
bme680.seal_level_pressure = 1013.25
start_time = time.time()
duration = 6
while  time.time() - start_time < duration:
	t = time.localtime()

	print(current_time, "\nTemperature: %0.1f C" % bme680.temperature, "Gas: %d ohm" % bme680.gas, "Humidity: %0.1f %%" % bme680.relative_humidity, "Pressure: %0.3f hPa" % bme680.pressure, "Altitude = %0.2f meters" % bme680.altitude)	
	time.sleep(2)
	
