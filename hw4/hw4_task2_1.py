"""HW4 - Task 2.1

Решето Эратосфена

Анализ:

Вариант с классической проверкой числа на простоту работает быстрее.
Сложность алгоритма O(n log (log n))
"""

import cProfile


def sieve(n):
    def _sieve(n):
        sieve = [i for i in range(n)]
        sieve[1] = 0
        for i in range(2, n):
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
        return [i for i in sieve if i != 0]
    i = 100
    result = _sieve(i)
    while len(result) < n:
        i += 50
        result = _sieve(i)
    return result[n - 1]

cProfile.run('sieve(500)')

'''
python -m timeit -n 1000 -s "import hw4_task2_1" "hw4_task2_1.sieve(500)"

sieve(10)
1000 loops, best of 5: 34.6 usec per loop

sieve(50)
1000 loops, best of 5: 287 usec per loop

sieve(200)
1000 loops, best of 5: 10.7 msec per loop

sieve(500)
1000 loops, best of 5: 107 msec per loop
'''

'''
cProfile.run('sieve(500)')

sieve(10)
1    0.000    0.000    0.000    0.000 hw4_task2_1.py:13(sieve)

sieve(50)
1    0.000    0.000    0.001    0.001 hw4_task2_1.py:13(sieve)

sieve(200)
1    0.000    0.000    0.013    0.013 hw4_task2_1.py:13(sieve)

sieve(500)
1    0.000    0.000    0.101    0.101 hw4_task2_1.py:13(sieve)
'''
