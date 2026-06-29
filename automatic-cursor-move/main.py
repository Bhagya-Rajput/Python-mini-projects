import pyautogui as pg
import random
import time
pg.FAILSAFE  = True
try:
    while True:
        x = random.randint(100,600)
        y = random.randint(100,600)
        pg.moveTo(x,y,0.5)
        time.sleep(2)
except pg.FailSafeException:
    print("program is now stopped")