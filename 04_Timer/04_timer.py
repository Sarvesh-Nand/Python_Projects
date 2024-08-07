from pydub import AudioSegment
from pydub.playback import play
import time
import os
import sys

def beep_alarm(beep_sound_path="beep-04.wav", num_beeps=7, interval=0.5):
    if not os.path.isfile(beep_sound_path):
        print(f"Error: The file {beep_sound_path} does not exist.")
        return

    beep_sound = AudioSegment.from_file(beep_sound_path)
    for _ in range(num_beeps):
        play(beep_sound)
        time.sleep(interval)  # Short pause between beeps

def clear_console():
    # Clear console screen for different OS
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        time_duration = int(input("Enter Duration in Seconds: "))
        if time_duration < 0:
            raise ValueError("Duration must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    hours, minutes, seconds = 0, 0, 0

    try:
        for _ in range(time_duration):
            clear_console()  # Clear the console
            seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1

            # Format time with leading zeros
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTimer interrupted!")
        sys.exit(0)

    beep_alarm()  # Call beep_alarm after timer finishes
    print("Time's up!")

if __name__ == '__main__':
    main()
