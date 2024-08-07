from pydub import AudioSegment
from pydub.playback import play
import time
import os
import sys

def beep_alarm(beep_sound_path="beep-04.wav"):
    if not os.path.isfile(beep_sound_path):
        print(f"Error: The file {beep_sound_path} does not exist.")
        return

    beep_sound = AudioSegment.from_file(beep_sound_path)
    for _ in range(7):
        play(beep_sound)
        time.sleep(0.5)  # Short pause between beeps

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

    beep_alarm()  # Call beep_alarm after timer finishes

if __name__ == '__main__':
    main()
