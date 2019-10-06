"""HW7 - Task 1

Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 100
array = [random.randrange(-size, size) for _ in range(13)]


def bubble(array):
    n = 1
    while n < len(array):
        swapped = False
        for i in range(len(array) - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        n += 1
        if not swapped:
            break


print(array)
bubble(array)
print(array)

'''
[-90, 84, 74, -30, 40, 48, -26, -25, -29, -67, 35, 34, -21]
[84, 74, 48, 40, 35, 34, -21, -25, -26, -29, -30, -67, -90]
'''
