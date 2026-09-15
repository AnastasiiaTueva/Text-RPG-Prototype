import sys 
import time
import msvcrt

#Function for text animation
def typetext(text, delay = 0.03):
    for i, char in enumerate(text):
        if msvcrt.kbhit():
            msvcrt.getch()
            sys.stdout.write(text[i:])
            sys.stdout.flush()
            print()
            return

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
