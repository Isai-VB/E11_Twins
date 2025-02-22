import sys
import time
import csv
import board
import serial
import adafruit_bme680
from adafruit_pm25.uart import PM25_UART

print(sys.argv)

if len(sys.argv) < 2:
    print("Script requires run_time(int) as an input")
    exit()
else:
    run_time = int(sys.argv[1])

# Initialize sensors
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25  

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
reset_pin = None  
pm25 = PM25_UART(uart, reset_pin)

filename = "Sensors.csv"
write_headers = not os.path.exists(filename)  # Check if file exists

# Open CSV file in append mode
with open(filename, "a", newline='') as file:
    file_writer = csv.writer(file)

    # Write headers only if the file is new
    if write_headers:
        file_writer.writerow(["Both Sensors Readings"])
        file_writer.writerow([
            "Current Time",
            "Temperature (C)", "Gas (ohm)", "Humidity (%)", "Pressure (hPa)", "Altitude (m)",
            "PM1.0 (standard)", "PM2.5 (standard)", "PM10 (standard)",
            "PM1.0 (env)", "PM2.5 (env)", "PM10 (env)",
            "Particles >0.3um", "Particles >0.5um", "Particles >1.0um",
            "Particles >2.5um", "Particles >5.0um", "Particles >10um"
        ])

    print("reading data...")
    start_time = time.time()

    while time.time() - start_time < run_time:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        temperature = bme680.temperature
        gas = bme680.gas
        humidity = bme680.relative_humidity
        pressure = bme680.pressure
        altitude = bme680.altitude

        try:
            aqdata = pm25.read()
        except RuntimeError:
            print("Unable to read from sensor, retrying...")
            time.sleep(1)
            continue

        # Extract data and write to CSV
        row = [
            current_time,
            temperature, gas, humidity, pressure, altitude,
            aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],
            aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"],
            aqdata["particles 03um"], aqdata["particles 05um"], aqdata["particles 10um"],
            aqdata["particles 25um"], aqdata["particles 50um"], aqdata["particles 100um"]
        ]
        file_writer.writerow(row)
        print("Logged data:", row)

        time.sleep(2)  # Wait 2 seconds before next reading
