"""HW3 - Task 9

Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

matrix = [[random.randint(-5, 5) for _ in range(8)] for _ in range(5)]

for row in matrix:
    for el in row:
        print(f'{el:>4}', end="")
    print()

column_mins = matrix[0][:]
for row in matrix[1:]:
    for i, el in enumerate(row):
        if column_mins[i] > el:
            column_mins[i] = el

print('*' * 34)
for _ in column_mins:
    print(f'{_:>4}', end="")
print('\tcolumn min\n')

max_el = column_mins[0]
for el in column_mins[1:]:
    if max_el < el:
        max_el = el
print(f'максимальный элемент среди минимальных: {max_el}')

'''OUTPUT
   1   5  -3  -5   5   4  -4   4
   3   4   5  -5   3   5   1  -4
   5  -3  -1   2   3  -1   4   3
   1   1  -2   5  -3  -3  -1  -3
   3   3  -5   2   2   0   1  -5
**********************************
   1  -3  -5  -5  -3  -3  -4  -5	column min

максимальный элемент среди минимальных: 1
'''
