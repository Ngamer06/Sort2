import timeit

code_to_test = """
import sys
from random import randint


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <=array[begin]:
            pivot +=1
            array[i], array[pivot] = array[pivot], array [i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

N = 10000
array = []
for i in range(N):
    array.append(randint(1,99999))

#print(array)
#quick_sort(array)
#print(array)
"""
elapsed_time = str(timeit.timeit(code_to_test, number=10)/10)
print("Быстрая сортировка " + elapsed_time)

code_to_test = """
import sys
from random import randint

def insert(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array [j] > item_to_insert:
            array[j + 1] = array [j]
            j -= 1
        array [j + 1] = item_to_insert

N = 10000
a = []
for i in range(N):
    a.append(randint(1,99999))

#print(a)
#insert(a)
#print (a)
"""
elapsed_time = str(timeit.timeit(code_to_test, number=10)/10)
print("Сортировка вставками " + elapsed_time)


code_to_test = """
import sys
from random import randint

def bubble(array):
    for i in range (N-1):
        for j in range(N-i-1):
            if array[j]>array[j+1]:
                buff = array[j]
                array[j] = a[j+1]
                array[j+1] = buff
N = 10000
a = []
for i in range(N):
    a.append(randint(1,99999))

#print(a)
#bubble(a)
#print (a)
"""
elapsed_time = str(timeit.timeit(code_to_test, number=10)/10)
print("Пузырьковая сортировка " + elapsed_time)
