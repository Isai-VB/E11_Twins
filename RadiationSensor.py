import RPi.GPIO as GPIO
import time
from datetime import datetime

# Define the GPIO pin connected to the sensor
SENSOR_PIN = 17  # Change this to the correct GPIO pin

# Initialize global variables
count = 0

def pulse_detected(channel):
    """Callback function triggered on falling edge detection."""
    global count
    count += 1
    print(f"Pulse detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor
GPIO.add_event_detect(SENSOR_PIN, GPIO.FALLING, callback=pulse_detected)

try:
    while True:
        time.sleep(60)  # Wait for a full minute
        print(f"Counts in the last minute: {count}")
        count = 0  # Reset count after each minute
except KeyboardInterrupt:
    print("Script terminated by user.")
    GPIO.cleanup()  # Cleanup GPIO settings before exiting
