from time import sleep

from draw_functions import draw_list
from utils import *


def bubble(list, window = None, canvas = None, low = None, high = None):
    size = len(list)
    for i in range(size-1):
        for j in range(size-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                if window and canvas:
                    draw_list(list, window, canvas, pointer = j + 1)


def insert(list, window = None, canvas = None, low = None, high = None):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
            list[j+1] = list[j]
            j -= 1
            if window and canvas:
                draw_list(list, window, canvas, pointer = j + 1)
        list[j+1] = key 


def quicksort_partition(list, low, high, window = None, canvas = None):
    i = ( low-1 )
    pivot = list[high]
    for j in range(low , high):
        if list[j] <= pivot:
            i = i+1
            if window and canvas:
                draw_list(list, window, canvas, pointer = i)
            list[i],list[j] = list[j],list[i]
    list[i+1],list[high] = list[high],list[i+1]
    if window and canvas:
        draw_list(list, window, canvas, pointer = i)
    return ( i+1 )

def quick(list, low = 0, high = 0, window = None, canvas = None):
    if low < high:
        pi = quicksort_partition(list, low, high, window = window, canvas = canvas)
        if window and canvas:
            draw_list(list, window, canvas, pointer = pi)
        quick(list, window = window, canvas = canvas, low = low, high = pi-1)
        quick(list, window = window, canvas = canvas, low = pi+1, high = high)


def merge_lists(arr, left_pointer, mid_point, right_pointer, window = None, canvas = None):
    n1 = mid_point - left_pointer + 1
    n2 = right_pointer - mid_point

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[left_pointer + i]
 
    for j in range(0, n2):
        R[j] = arr[mid_point + 1 + j]
 
    i = 0
    j = 0
    pointer = left_pointer
    if window and canvas:
        draw_list(arr, window, canvas, pointer = pointer + 1)

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[pointer] = L[i]
            i += 1
        else:
            arr[pointer] = R[j]
            j += 1
        pointer += 1
        if window and canvas:
            draw_list(arr, window, canvas, pointer = pointer + 1)

    while i < n1:
        arr[pointer] = L[i]
        i += 1
        pointer += 1

    while j < n2:
        arr[pointer] = R[j]
        j += 1
        pointer += 1


def merge(arr, low = 0, high = 0, window = None, canvas = None):
    left_pointer, right_pointer = low, high
    if left_pointer < right_pointer:
        mid_point = left_pointer + (right_pointer - left_pointer) // 2
 
        merge(arr, left_pointer, mid_point, window = window, canvas = canvas)
        merge(arr, mid_point+1, right_pointer, window = window, canvas = canvas)
        merge_lists(arr, left_pointer, mid_point, right_pointer, window = window, canvas = canvas)
 