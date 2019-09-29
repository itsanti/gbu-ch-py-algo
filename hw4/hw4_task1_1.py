"""HW4 - Task 1.1

Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

Анализ:

Вариант с циклом быстрее почти в 2 раза чем рекурсия и не зависит от глубины рекурсии.
Сложность алгоритма O(n)
"""

import cProfile
import functools


@functools.lru_cache()
def accsumm(n):
    if n == 0:
        return 0

    return 1 + accsumm(n - 1) / -2


cProfile.run('accsumm(400)')

'''
python -m timeit -n 1000 -s "import hw4_task1_1" "hw4_task1_1.accsumm(400)"

accsumm(5)
1000 loops, best of 5: 1.11 usec per loop

accsumm(10)
1000 loops, best of 5: 2.12 usec per loop

accsumm(20)
1000 loops, best of 5: 4.29 usec per loop

accsumm(40)
1000 loops, best of 5: 8.62 usec per loop

accsumm(100)
1000 loops, best of 5: 21.5 usec per loop

accsumm(200)
1000 loops, best of 5: 45.4 usec per loop

accsumm(400)
1000 loops, best of 5: 112 usec per loop
'''

'''
cProfile.run('accsumm(400)')

accsumm(5)
6/1    0.000    0.000    0.000    0.000 hw4_task1_1.py:8(accsumm)

accsumm(40)
41/1    0.000    0.000    0.000    0.000 hw4_task1_1.py:8(accsumm)

accsumm(200)
201/1    0.000    0.000    0.000    0.000 hw4_task1_1.py:8(accsumm)

accsumm(400)
401/1    0.000    0.000    0.000    0.000 hw4_task1_1.py:8(accsumm)
'''

'''
@functools.lru_cache()

accsumm(400)
401/1    0.001    0.000    0.001    0.001 hw4_task1_1.py:10(accsumm)
'''