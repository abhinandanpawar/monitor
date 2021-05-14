import pyautogui
import time 
import threading
import random


print("Enter your name")
user=input()
print("Enter Project name")
project=input()

name=user+" "+project


def shott(name):
    screenshot = pyautogui.screenshot()
    screenshot.save("shots\%s.png" %name)

def timer():
    halt=random.randint(1, 10)
    ti = time.gmtime()
    print (str(halt)+str((time.asctime(ti))))
 

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=shott, args=(name,))
    t2 = threading.Thread(target=timer)
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")

