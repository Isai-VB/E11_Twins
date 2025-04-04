import RPi.GPIO as GPIO
import time

# Set up GPIO pin for radiation sensor
SENSOR_PIN = 17  # Change this to the GPIO pin you're using
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Global variables
count_per_second = 0
total_count = 0

# Callback function for detecting pulses
def pulse_detected(channel):
    global count_per_second, total_count
    count_per_second += 1
    total_count += 1

# Attach event detection
GPIO.add_event_detect(SENSOR_PIN, GPIO.FALLING, callback=pulse_detected)

try:
    while True:
        for i in range(60):  # Loop for 60 seconds
            count_per_second = 0  # Reset count every second
            time.sleep(1)  # Wait for a second
            print(f"Second {i+1}: {count_per_second} counts")  # Print count for that second

        print(f"Total counts in last 60 seconds: {total_count}")  # Print total count for the minute
        total_count = 0  # Reset total count for the next minute

except KeyboardInterrupt:
    print("\nStopping script...")
    GPIO.cleanup()  # Clean up GPIO on exit
