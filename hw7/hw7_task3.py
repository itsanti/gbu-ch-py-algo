"""HW7 - Task 3

Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

import random
#from statistics import median

size = 6
array = [random.randint(0, 50) for _ in range(2 * size + 1)]


def radix(array):
    RADIX = 10
    placement = 1
    max_digit = max(array)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]

        for i in array:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1

        placement *= RADIX


def median(array):
    return array[((len(array) - 1) // 2)]


print(array)
radix(array)
print(median(array))
print(array)

'''
[16, 47, 50, 8, 8, 39, 15, 21, 22, 34, 43, 22, 43]
22
[8, 8, 15, 16, 21, 22, 22, 34, 39, 43, 43, 47, 50]
'''
