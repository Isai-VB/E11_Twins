# E11_Twins
error: The following untracked working tree files would be overwritten by merge:
	SensorsInside.csv
Please move or remove them before you merge.
Aborting
['test_inputs.py', '50']
Reading data...
Traceback (most recent call last):
  File "/home/pi/E11_Twins/test_inputs.py", line 50, in <module>
    temp = bme680.temperature
  File "/home/pi/.local/lib/python3.9/site-packages/adafruit_bme680.py", line 277, in temperature
    self._perform_reading()
  File "/home/pi/.local/lib/python3.9/site-packages/adafruit_bme680.py", line 398, in _perform_reading
    ctrl = self._read_byte(_BME680_REG_CTRL_MEAS)
  File "/home/pi/.local/lib/python3.9/site-packages/adafruit_bme680.py", line 450, in _read_byte
    return self._read(register, 1)[0]
  File "/home/pi/.local/lib/python3.9/site-packages/adafruit_bme680.py", line 681, in _read
    i2c.readinto(result)
  File "/home/pi/.local/lib/python3.9/site-packages/adafruit_bus_device/i2c_device.py", line 81, in readinto
    self.i2c.readfrom_into(self.device_address, buf, start=start, end=end)
  File "/home/pi/.local/lib/python3.9/site-packages/busio.py", line 197, in readfrom_into
    return self._i2c.readfrom_into(address, buffer, stop=True)
  File "/home/pi/.local/lib/python3.9/site-packages/adafruit_blinka/microcontroller/generic_linux/i2c.py", line 67, in readfrom_into
    readin = self._i2c_bus.read_bytes(address, end - start)
  File "/home/pi/.local/lib/python3.9/site-packages/Adafruit_PureIO/smbus.py", line 170, in read_bytes
    return self._device.read(number)
OSError: [Errno 121] Remote I/O error
