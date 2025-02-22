import csv
import time
import serial
from adafruit_pm25.uart import PM25_UART

# Initialize UART connection to PM2.5 sensor
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
reset_pin = None  # Adjust if using a reset pin
pm25 = PM25_UART(uart, reset_pin)

# Open CSV file for writing
filename = "pm25_data.csv"
with open(filename, "w", newline='') as file:
    file_writer = csv.writer(file)
    
    # Write meta-data line
    file_writer.writerow(["PM2.5 Sensor Data Log - Captured Readings with Timestamps"])
    
    # Write CSV headers
    file_writer.writerow([
        "Timestamp", "PM1.0 (standard)", "PM2.5 (standard)", "PM10 (standard)",
        "PM1.0 (env)", "PM2.5 (env)", "PM10 (env)",
        "Particles >0.3um", "Particles >0.5um", "Particles >1.0um",
        "Particles >2.5um", "Particles >5.0um", "Particles >10um"
    ])

    print("Found PM2.5 sensor, reading data...")
    start_time = time.time()
    duration = 60  # Run for 60 seconds
    
    while time.time() - start_time < duration:
        time.sleep(1)
        try:
            aqdata = pm25.read()
        except RuntimeError:
            print("Unable to read from sensor, retrying...")
            continue

        # Get current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        # Extract data and write to CSV
        row = [
            timestamp,
            aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"],
            aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"],
            aqdata["particles 03um"], aqdata["particles 05um"], aqdata["particles 10um"],
            aqdata["particles 25um"], aqdata["particles 50um"], aqdata["particles 100um"]
        ]
        file_writer.writerow(row)
        print("Logged data:", row)
