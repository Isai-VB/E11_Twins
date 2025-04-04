import RPi.GPIO as GPIO
import time

# Set up GPIO pin for radiation sensor
SENSOR_PIN = 17  # Change this to the GPIO pin you're using
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Global variable to store the total count
total_count = 0

# Callback function for detecting pulses
def pulse_detected(channel):
    global total_count
    total_count += 1

# Attach event detection
GPIO.add_event_detect(SENSOR_PIN, GPIO.FALLING, callback=pulse_detected)

def run_for_duration(run_time, count_interval, output_file):
    global total_count
    try:
        start_time = time.time()
        end_time = start_time + run_time  # Set the run duration
        current_time = time.time()

        with open(output_file, 'w') as file:
            file.write("Timestamp,Count\n")  # Header for the output file

            while current_time < end_time:
                interval_end_time = time.time() + count_interval

                while time.time() < interval_end_time:
                    # Wait for the interval time to pass
                    pass
                
                # Write the current count and timestamp to the file
                timestamp = time.time()
                file.write(f"{timestamp},{total_count}\n")
                print(f"Timestamp: {timestamp}, Count: {total_count}")
                
                # Reset the total count for the next interval
                total_count = 0
                current_time = time.time()

    except KeyboardInterrupt:
        print("\nStopping script...")
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    # Automatically set runtime to 120 seconds (2 minutes) and count interval to 1 second
    run_time = 120
    count_interval = 1
    output_file = "radiation_data.csv"  # Output file name

    # Run the script with the pre-defined values
    run_for_duration(run_time, count_interval, output_file)
