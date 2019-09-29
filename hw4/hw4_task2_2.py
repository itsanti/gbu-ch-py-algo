"""HW4 - Task 2.2

классическая проверка числа на простоту

Анализ:

Вариант с классической проверкой числа на простоту работает быстрее.
Сложность алгоритма O(sqrt(n))
"""

import cProfile
from math import sqrt


def prime(n):
    def is_prime(n):
        i = 2
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i += 1
        return True
    result = []
    first = 2
    size = 50
    while len(result) < n:
        for k in range(first, size):
            if is_prime(k):
                result.append(k)
        first = size
        size *= 2
    return result[n - 1]


cProfile.run('prime(500)')

'''
python -m timeit -n 1000 -s "import hw4_task2_2" "hw4_task2_2.prime(500)"

sieve(10)
1000 loops, best of 5: 32 usec per loop

sieve(50)
1000 loops, best of 5: 443 usec per loop

sieve(200)
1000 loops, best of 5: 2.68 msec per loop

sieve(500)
1000 loops, best of 5: 17.3 msec per loop
'''

'''
cProfile.run('prime(500)')

prime(10)
 1    0.000    0.000    0.000    0.000 hw4_task2_2.py:14(prime)
48    0.000    0.000    0.000    0.000 hw4_task2_2.py:15(is_prime)

prime(50)
  1    0.000    0.000    0.001    0.001 hw4_task2_2.py:14(prime)
398    0.000    0.000    0.001    0.000 hw4_task2_2.py:15(is_prime)

prime(200)
   1    0.000    0.000    0.004    0.004 hw4_task2_2.py:14(prime)
1598    0.002    0.000    0.003    0.000 hw4_task2_2.py:15(is_prime)

prime(500)
   1    0.001    0.001    0.025    0.025 hw4_task2_2.py:14(prime)
6398    0.016    0.000    0.024    0.000 hw4_task2_2.py:15(is_prime)
'''
