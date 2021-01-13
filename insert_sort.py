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