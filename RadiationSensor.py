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

def run_for_duration(run_time, count_interval, output_file):
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
    # Ask for user input
    run_time = int(input("Enter the total runtime in seconds: "))
    count_interval = int(input("Enter the count interval in seconds: "))
    output_file = input("Enter the output file name (e.g., 'radiation_data.csv'): ")

    # Run the script with the provided input values
    run_for_duration(run_time, count_interval, output_file)
