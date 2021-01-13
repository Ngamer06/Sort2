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