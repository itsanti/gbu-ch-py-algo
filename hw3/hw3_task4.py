"""HW3 - Task 4

Определить, какое число в массиве встречается чаще всего.
"""

import random

in_arr = [random.randint(-3, 3) for _ in range(10)]
print(in_arr)

d = {}
count = 0
for el in in_arr:
    d[el] = d.get(el, 0) + 1
    count = d[el] if d[el] > count else count

if count > 1:
    for k, val in d.items():
        if val == count:
            print(f'число {k} встречается чаще всего')
else:
    print('все числа встречаются 1 раз')

'''OUTPUT
[0, 2, 3, -2, -1, 2, 2, -1, -1, 3]
число 2 встречается чаще всего
число -1 встречается чаще всего

[3, 1, -1, 2, 3, -2, -2, 3, 1, 0]
число 3 встречается чаще всего
'''
