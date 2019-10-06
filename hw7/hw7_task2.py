"""HW7 - Task 2

Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 50
array = [round(random.uniform(0, size), 3) for _ in range(13)]


def merge(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge(left)
        merge(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        return array


print(array)
merge(array)
print(array)

'''
[42.901, 32.897, 37.576, 38.03, 10.401, 23.694, 10.099, 16.284, 49.784, 3.927, 22.102, 14.853, 36.551]
[3.927, 10.099, 10.401, 14.853, 16.284, 22.102, 23.694, 32.897, 36.551, 37.576, 38.03, 42.901, 49.784]
'''
