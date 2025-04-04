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
    start_time = time.time()  # Record the start time
    while True:
        current_time = time.time()  # Get the current time
        elapsed_time = current_time - start_time  # Calculate elapsed time

        if elapsed_time >= 60:  # Stop the loop after 60 seconds
            break

        # Reset the count per second
        count_per_second = 0
        time.sleep(1)  # Wait for 1 second
        print(f"Second {int(elapsed_time)+1}: {count_per_second} counts")  # Print counts for the second

    print(f"Total counts in last 60 seconds: {total_count}")  # Print total count for the minute

except KeyboardInterrupt:
    print("\nStopping script...")
    GPIO.cleanup()  # Clean up GPIO on exit
