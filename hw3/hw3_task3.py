"""HW3 - Task 3

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

in_arr = [random.randint(-10, 10) for _ in range(5)]
print(in_arr)

min_el = max_el = (0, in_arr[0])
for i, el in enumerate(in_arr):
    if el > max_el[1]:
        max_el = (i, el)
    if el < min_el[1]:
        min_el = (i, el)

in_arr[min_el[0]], in_arr[max_el[0]] = max_el[1], min_el[1]
print(in_arr)

'''OUTPUT
[2, -10, 8, -8, 3]
[2, 8, -10, -8, 3]

[-7, 8, 8, -1, 5]
[8, -7, 8, -1, 5]

[6, -6, 6, -9, 8]
[6, -6, 6, 8, -9]
'''
