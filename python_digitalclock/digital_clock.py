# digital_clock.py

import time

def run_digital_clock():
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print("Current Time:", current_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    run_digital_clock()

