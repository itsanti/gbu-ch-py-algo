"""HW4 - Task 1.2

Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

Анализ:

Вариант с циклом быстрее почти в 2 раза чем рекурсия и не зависит от глубины рекурсии.
Сложность алгоритма O(n)
"""
import cProfile

def accsumm(n):
    a = 1
    i = 0
    summa = 0
    while i < n:
        summa += a
        a = a / -2
        i += 1
    return summa


cProfile.run('accsumm(400)')

'''
python -m timeit -n 1000 -s "import hw4_task1_2" "hw4_task1_2.accsumm(400)"

accsumm(5)
1000 loops, best of 5: 922 nsec per loop

accsumm(10)
1000 loops, best of 5: 1.53 usec per loop

accsumm(20)
1000 loops, best of 5: 2.8 usec per loop

accsumm(40)
1000 loops, best of 5: 5.33 usec per loop

accsumm(100)
1000 loops, best of 5: 13.3 usec per loop

accsumm(200)
1000 loops, best of 5: 26.5 usec per loop

accsumm(400)
1000 loops, best of 5: 62.4 usec per loop
'''

'''
cProfile.run('accsumm(400)')

accsumm(5)
1    0.000    0.000    0.000    0.000 hw4_task1_2.py:7(accsumm)

accsumm(400)
1    0.000    0.000    0.000    0.000 hw4_task1_2.py:7(accsumm)
'''