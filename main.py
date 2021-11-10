import tkinter
import random
from time import time
import matplotlib.pyplot as plt
import numpy as np

from draw_functions import draw_list
import sort_functions
from utils import *


time_mode = True


list_unsorted = [i for i in range(100)]
random.shuffle(list_unsorted)

def begin_bubble(visual = True):
    start_time = time()
    random.shuffle(list_unsorted)
    if visual:
        draw_list(list_unsorted, window, canvas, done = False)
    sort_functions.bubble(list_unsorted, window = window if visual else None, canvas = canvas if visual else None)
    if visual:
        draw_list(list_unsorted, window, canvas, done = True)
    return time() - start_time

def begin_insert(visual = True):
    start_time = time()
    random.shuffle(list_unsorted)
    if visual:
        draw_list(list_unsorted, window, canvas, done = False)
    sort_functions.insert(list_unsorted, window = window if visual else None, canvas = canvas if visual else None)
    if visual:
        draw_list(list_unsorted, window, canvas, done = True)
    return time() - start_time

def begin_quick(visual = True):
    start_time = time()
    random.shuffle(list_unsorted)
    if visual:
        draw_list(list_unsorted, window, canvas, done = False)
    sort_functions.quick(list_unsorted, 0, len(list_unsorted) - 1, window = window if visual else None, canvas = canvas if visual else None)
    if visual:
        draw_list(list_unsorted, window, canvas, done = True)
    return time() - start_time

def begin_merge(visual = True):
    start_time = time()
    random.shuffle(list_unsorted)
    if visual:
        draw_list(list_unsorted, window, canvas, done = False)
    sort_functions.merge(list_unsorted, 0, len(list_unsorted) - 1, window = window if visual else None, canvas = canvas if visual else None)
    if visual:
        draw_list(list_unsorted, window, canvas, done = True)
    return time() - start_time

if time_mode:
    bubble, insert, quick, merge = [], [], [], []
    list_range = np.arange(100, 1001, 10)
    for list_len in list_range:
        list_unsorted = [i for i in range(list_len)]
        random.shuffle(list_unsorted)
        bubble.append(begin_bubble(visual=False) * 1000)
        insert.append(begin_insert(visual=False) * 1000)
        quick.append(begin_quick(visual=False) * 1000)
        merge.append(begin_merge(visual=False) * 1000)

        print(f"Plotted list size {list_len} data")
    
    plt.scatter(np.array(bubble), list_range, label = "Bubble Sort", s = 10)
    plt.scatter(np.array(insert), list_range, label = "Insert Sort", s = 10)
    plt.scatter(np.array(quick), list_range, label = "Quick Sort", s = 10)
    plt.scatter(np.array(merge), list_range, label = "Merge Sort", s = 10)
    
    plt.xlabel("Time taken to sort (ms)")
    plt.ylabel("List size")
    plt.title("Sorting Algorithm Comparison")
    plt.legend()
    plt.show()

else:
    window = tkinter.Tk()
    window.title("Sort Comparison")
    window.config(bg = light_gray)

    UI_frame = tkinter.Frame(window, width= 900, height=300, bg=white)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    sort_methods = [begin_bubble, begin_insert, begin_quick, begin_merge]
    
    for index, method in enumerate(['bubble', 'insert', 'quick', 'merge']):
        button = tkinter.Button(UI_frame, text=method, command=sort_methods[index], bg=light_gray)
        button.grid(row=1, column=index, padx=5, pady=5)

    canvas = tkinter.Canvas(window, width = 800, height = 400, bg = light_gray)
    canvas.grid(row = 1, column= 0, padx = 10, pady = 5)

    draw_list(list_unsorted, window, canvas)
    window.mainloop()