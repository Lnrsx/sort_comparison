import tkinter
import random
from time import time
import matplotlib.pyplot as plt
import numpy as np

from draw_functions import draw_list
import sort_functions
from utils import *


time_mode = False


list_unsorted = [i for i in range(100)]
random.shuffle(list_unsorted)

sort_types = {
    "Bubble": sort_functions.bubble,
    "Insert": sort_functions.insert,
    "Quick": sort_functions.quick,
    "Merge": sort_functions.merge
}

def begin_sort(type, visual = True):
    start_time = time()
    random.shuffle(list_unsorted)
    if visual:
        draw_list(list_unsorted, window, canvas, done = False)
    sort_types[type](list_unsorted, window = window if visual else None, canvas = canvas if visual else None, low = 0, high = len(list_unsorted) - 1)
    if visual:
        draw_list(list_unsorted, window, canvas, done = True)
    return time() - start_time

if time_mode:
    sort_data = {
        "Bubble": [],
        "Insert": [],
        "Quick": [],
        "Merge": []
    }
    list_range = np.arange(100, 1001, 10)
    for list_len in list_range:
        list_unsorted = [i for i in range(list_len)]

        for method, time_list in sort_data.items():
            time_list.append(begin_sort(method, visual=False) * 1000)

        print(f"Plotted list size {list_len} data")
    
    for method, time_list in sort_data.items():
        plt.scatter( list_range, np.array(time_list), label = f"{method} Sort", s = 10)
    
    plt.xlabel("List Size")
    plt.ylabel("Time taken to sort (ms)")
    plt.title("Sorting Algorithm Comparison")
    plt.legend()
    plt.show()

else:
    window = tkinter.Tk()
    window.title("Sort Comparison")
    window.config(bg = light_gray)

    UI_frame = tkinter.Frame(window, width= 900, height=300, bg=white)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    canvas = tkinter.Canvas(window, width = 800, height = 400, bg = light_gray)
    canvas.grid(row = 1, column= 0, padx = 10, pady = 5)
    
    for index, (method, function) in enumerate(sort_types.items()):
        button = tkinter.Button(UI_frame, text=method, command=lambda m=method: begin_sort(m), bg=light_gray)
        button.grid(row=1, column=index, padx=5, pady=5)

    draw_list(list_unsorted, window, canvas)
    window.mainloop()