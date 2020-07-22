import tkinter as tk
import pyautogui
import random
import math
import os
import datetime
import pathlib

RUNNING = False
BUTTON_AFTER_ID = None
pyautogui.FAILSAFE = False
START_TIME = datetime.datetime.now()


def start_moving(root, start_button, stop_button, timer_label, position_label):
    global RUNNING, START_TIME
    RUNNING = True
    START_TIME = datetime.datetime.now()
    moving(root, start_button, stop_button, timer_label, position_label)


def moving(root, start_button, stop_button, timer_label, position_label):
    global RUNNING, BUTTON_AFTER_ID, START_TIME
    if RUNNING:
        start_button['state'] = 'disabled'
        stop_button['state'] = 'normal'
        current_screen_width, current_screen_height = pyautogui.size()
        move_to_x = math.floor(current_screen_width *
                               (random.randint(1, current_screen_width) / current_screen_width))
        move_to_y = math.floor(current_screen_height *
                               (random.randint(1, current_screen_height) / current_screen_height))
        pyautogui.moveTo(move_to_x, move_to_y)
        elapsed_time = (datetime.datetime.now() - START_TIME).total_seconds()
        timer_label['text'] = 'Time Elapsed: %s seconds' % math.floor(elapsed_time)
        position_label['text'] = 'x: %s, y: %s' % pyautogui.position()
        BUTTON_AFTER_ID = root.after(5000, lambda: moving(root, start_button, stop_button, timer_label, position_label))


def stop_moving(root, start_button, stop_button, timer_label, position_label):
    global RUNNING, BUTTON_AFTER_ID
    RUNNING = False
    BUTTON_AFTER_ID = None
    start_button['state'] = 'normal'
    stop_button['state'] = 'disable'
    timer_label['text'] = 'Click Start to Begin'
    position_label['text'] = 'x: %s, y: %s' % pyautogui.position()


def build_interface():
    root = tk.Tk()
    root.title('Mouse Wanderer')
    root.minsize(width=350, height=200)
    root.maxsize(width=350, height=200)
    imgicon = tk.PhotoImage(file=os.path.join(pathlib.Path(__file__).parent.absolute(), 'icon.png'))
    root.tk.call('wm', 'iconphoto', root._w, imgicon)
    main_frame = tk.Frame(root)
    main_frame.pack(anchor='center', padx=20, pady=10, expand=True)
    indicator_frame = tk.Frame(main_frame)
    indicator_frame.pack(anchor='n', expand=True)
    controller_frame = tk.Frame(main_frame)
    controller_frame.pack(anchor='s', expand=True)
    timer_label = tk.Label(master=indicator_frame, text='Click Start to Begin', fg='gray9', font='Helvetica 25 normal')
    timer_label.pack(side='top')
    position_label = tk.Label(master=indicator_frame, text='x: %s, y: %s' % pyautogui.position(), fg='gray9',
                              font='Helvetica 20 normal')
    position_label.pack(side='bottom')
    start_button = tk.Button(master=controller_frame, text='Start', width=10)
    start_button.pack(side='left')
    stop_button = tk.Button(master=controller_frame, text='Stop', width=10)
    stop_button.pack(side='right')
    start_button['command'] = lambda: start_moving(root, start_button, stop_button, timer_label, position_label)
    stop_button['command'] = lambda: stop_moving(root, start_button, stop_button, timer_label, position_label)
    start_button['state'] = 'normal'
    stop_button['state'] = 'disabled'
    root.mainloop()


if __name__ == '__main__':
    build_interface()
