# alaram clock
import time
import datetime
import pygame

def set_alarm():
    print(f"Alarm set for {alarm__time}")
    sound_file = "clock-220860.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm__time:
            print("😴 WAKE UP ⏰")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False

        time.sleep(1)




if __name__ == "__main__":

    alarm__time = input("Enter an alarm time (Hour:minute:Second)⏰: ")
    set_alarm()