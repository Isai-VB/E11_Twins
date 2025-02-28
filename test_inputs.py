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

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25  

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
reset_pin = None  
pm25 = PM25_UART(uart, reset_pin)

# Open CSV file 
filename = "NewSensors.csv"
with open(filename, "w", newline='') as file:
    file_writer = csv.writer(file)
    
    # Meta-data line
    file_writer.writerow(["Both Sensors Readings"])
    
    # Write CSV Headers
    file_writer.writerow([
        "Time",
        "Temp", "Gas", "Humidity", "Pressure", "Altitude",
        "PM1.0std", "PM2.5std", "PM10std",
        "PM1.0env", "PM2.5env", "PM10env",
        "Particles 0.3um", "Particles 0.5um", "Particles 1.0um",
        "Particles 2.5um", "Particles 5.0um", "Particles 10um"
    ])

    print("Reading data...")
    
    start_time = time.time()
    
    while time.time() - start_time < run_time:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        temp = bme680.temperature
        gas = bme680.gas
        humidity = bme680.relative_humidity
        pressure = bme680.pressure
        altitude = bme680.altitude

        try:
            aqdata = pm25.read()
        except RuntimeError:
            print("Unable to read from sensor, retrying...")
            time.sleep(1)  # Wait before retrying
            continue

        # Extract data and write to CSV
        row = [
            current_time,
            temp, gas, humidity, pressure, altitude,
            aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],
            aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"],
            aqdata["particles 0.3um"], aqdata["particles 0.5um"], aqdata["particles 1.0um"],
            aqdata["particles 2.5um"], aqdata["particles 5.0um"], aqdata["particles 10um"]
        ]
        file_writer.writerow(row)
        print("Logged data:", row)

        time.sleep(2)  # Wait 2 seconds before the next reading
