import pyautogui
import subprocess
from time import sleep
from math import floor
import random



class MouseWandererManualStoppingException(Exception):
    def __init__(self, message='Mouse wanderer has been stopped manually'):
        self.message = message

    def __str__(self):
        return self.message



def main(move_type):
    BACKGROUND_APP = 'C:\WINDOWS\system32\mspaint.exe'
    APP_OPEN_WAIT_TIME = 2
    pyautogui.PAUSE = 5
    pyautogui.FAILSAFE = True
    FAILSAFE_TOPLEFT_AREA_FACTOR = 0.1
    CENTER_FACTOR = 0.333
    WANDER_RANGE_FACTOR = 0.1

    # open up process
    app_process = subprocess.Popen([BACKGROUND_APP])
    sleep(APP_OPEN_WAIT_TIME)
    pyautogui.hotkey('win', 'up')

    initial_screenWidth, initial_screenHeight = pyautogui.size()
    pyautogui.FAILSAFE_POINTS = get_failsafe_top_left_area_points(initial_screenWidth, initial_screenHeight,
                                                                  FAILSAFE_TOPLEFT_AREA_FACTOR)
    print("Screen Width: %s, Screen Height: %s" % (initial_screenWidth, initial_screenHeight))
    currentX, currentY = pyautogui.position()
    print("Current Position: (X: %s, Y: %s)" % pyautogui.position())
    try:
        while True:
            if pyautogui.size() != (initial_screenWidth, initial_screenHeight):
                initial_screenWidth, initial_screenHeight = pyautogui.size()
                print("Screen Size Changed, Current Width: %s, Current Height: %s" % (
                initial_screenWidth, initial_screenHeight))
                pyautogui.FAILSAFE_POINTS = get_failsafe_top_left_area_points(initial_screenWidth, initial_screenHeight,
                                                                              FAILSAFE_TOPLEFT_AREA_FACTOR)
            pyautogui.moveTo(floor(initial_screenWidth * CENTER_FACTOR), floor(initial_screenHeight * CENTER_FACTOR))
            print("Moved To: (X: %s, Y: %s)" % pyautogui.position())
            next_x = random.randint(-floor(initial_screenWidth * WANDER_RANGE_FACTOR),
                                    floor(initial_screenWidth * WANDER_RANGE_FACTOR))
            next_y = random.randint(-floor(initial_screenHeight * WANDER_RANGE_FACTOR),
                                    floor(initial_screenHeight * WANDER_RANGE_FACTOR))
            if move_type == 'DRAG':
                pyautogui.drag(next_x, next_y, duration=(random.randint(1, 2000) / 2000))
            elif move_type == 'MOVE_REL':
                pyautogui.moveRel(next_x, next_y, duration=(random.randint(1, 2000) / 2000))
            else:
                raise RuntimeError('The move type is not supported.')
            print("Dragged To: (X: %s, Y: %s)" % (next_x, next_y))

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
    MOVE_TYPE = 'DRAG'
    # can be change to 'MOVE_REL'
    main(MOVE_TYPE)
