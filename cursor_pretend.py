from pyautogui import moveTo, press
import random
import time
import os
from sys import argv
from datetime import datetime

path = ''

def shut_down(leave = False):
    if leave == True:
        os.system('shutdown -s -t 0')
    else:
        pass

def time_to_leave(leaving_time):
    now = datetime.now()
    if now.hour >= leaving_time:
        shut_down(True)
    else:
        shut_down(False)


input_file = 'sample_text'
with open(path+input_file+'.txt', 'r') as f:
    for line in f:
        lines_list = [line.replace('\n', '') for line in f if line not in ['', ' ', '    ']]
list_length = len(lines_list)

def pretend_function(duration, leaving = False, leaving_time = 19):
    for i in range(duration):
        printed_line = lines_list[random.randint(0, list_length-1)]
        now = datetime.now().strftime('%H:%M')
        print(f'Iteración: {i}. Para detener el programa presione ctrl + c\n Linea escrita: {printed_line}. @{now}')
        x = random.randint(700, 1400)
        y = random.randint(300, 700)
        moveTo(x, y, duration=3)
        iterator_object = [w for w in printed_line if w not in ['', '    ']]
        for letter in iterator_object:
            press(letter)
            time.sleep(0.125)
        time.sleep(60)
    if leaving == True:
        time_to_leave(leaving_time)
    else:
        pass

if __name__=="__main__":
    if len(argv) == 4:
        pretend_function(int(argv[1]), bool(argv[2]), int(argv[3]))
    else:
        pretend_function(int(argv[1]))
