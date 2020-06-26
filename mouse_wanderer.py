import pyautogui
import subprocess
from time import sleep
from math import floor
import random

def main():
    BACKGROUND_APP = 'C:\WINDOWS\system32\mspaint.exe'
    APP_OPEN_WAIT_TIME = 2
    pyautogui.PAUSE = 5
    pyautogui.FAILSAFE = True
    FAILSAFE_TOPLEFT_AREA_FACTOR = 0.1

    # open up process
    app_process = subprocess.Popen([BACKGROUND_APP])
    sleep(APP_OPEN_WAIT_TIME)
    pyautogui.hotkey('win', 'up')

    screenWidth, screenHeight = pyautogui.size()
    pyautogui.FAILSAFE_POINTS.extend(get_failsafe_top_left_area_points(screenWidth, screenHeight, FAILSAFE_TOPLEFT_AREA_FACTOR))
    print("Screen Width: %s, Screen Height: %s" % (screenWidth, screenHeight))
    currentX, currentY = pyautogui.position()
    print("Current Position: (X: %s, Y: %s)" % pyautogui.position())
    try:
        while True:
            INITIAL_POSITION = (screenWidth // 3, screenHeight // 3)
            pyautogui.moveTo(INITIAL_POSITION[0], INITIAL_POSITION[1])
            print("Moved To: (X: %s, Y: %s)" % pyautogui.position())
            next_x = random.randint(-screenWidth // 10, screenWidth // 10)
            next_y = random.randint(-screenHeight // 10, screenHeight // 10)
            pyautogui.drag(next_x, next_y, duration=(random.randint(1, 2000)/2000))
            print("dragged")

    except pyautogui.FailSafeException:
        print("Fail Safe exit")
    finally:
        pyautogui.alert(text='You are about to exit', title='Confirm Exit', button='OK')
        app_process.kill()


def get_failsafe_top_left_area_points(screenWidth, screenHeight, factor):
    result = []
    for x in range(floor(screenWidth * factor)):
        for y in range(floor(screenWidth * factor)):
            result.append((x, y))
    return result


if __name__ == '__main__':
    main()
