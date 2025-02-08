import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25  

duration = 10  
start_time = time.time()

while time.time() - start_time < duration:
    current_time = time.strftime("%H:%M:%S", time.localtime())

    temperature = bme680.temperature
    gas = bme680.gas
    humidity = bme680.relative_humidity
    pressure = bme680.pressure
    altitude = bme680.altitude


    print(f"\rcurrent time: {current_time} | Temperature: {bme680.temperature:.1f} C | Gas: {bme680.gas} ohm | Humidity: {bme680.relative_humidity:.1f}% | Pressure: {bme680.pressure:.3f} hPa | Altitude: {bme680.altitude:.2f} meters")


    time.sleep(2)  # Wait 2 seconds before next reading
