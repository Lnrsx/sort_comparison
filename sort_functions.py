from time import sleep

from draw_functions import draw_list
from utils import *


def bubble(list, window = None, canvas = None):
    size = len(list)
    for i in range(size-1):
        for j in range(size-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                if window and canvas:
                    draw_list(list, window, canvas, pointer = j + 1)


def insert(list, window = None, canvas = None):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
            list[j+1] = list[j]
            j -= 1
            if window and canvas:
                draw_list(list, window, canvas, pointer = j + 1)
        list[j+1] = key 


def quicksort_partition(list, low, high):
   i = ( low-1 )
   pivot = list[high]
   for j in range(low , high):
      if list[j] <= pivot:
         i = i+1
         list[i],list[j] = list[j],list[i]
   list[i+1],list[high] = list[high],list[i+1]
   return ( i+1 )

def quick(list, low, high, window = None, canvas = None):
    if low < high:
        pi = quicksort_partition(list, low, high)
        quick(list, low, pi-1, window, canvas)
        quick(list, pi+1, high, window, canvas)
        if window and canvas:
            draw_list(list, window, canvas, pointer = pi)


def merge_lists(arr, l, m, r, window = None, canvas = None):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0
    j = 0
    k = l
    if window and canvas:
        draw_list(arr, window, canvas, pointer = k + 1)

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        if window and canvas:
            draw_list(arr, window, canvas, pointer = k + 1)

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 

def merge(arr, l, r, window = None, canvas = None):
    if l < r:
        m = l+(r-l)//2
 
        merge(arr, l, m, window = window, canvas = canvas)
        merge(arr, m+1, r, window = window, canvas = canvas)
        merge_lists(arr, l, m, r, window = window, canvas = canvas)
 