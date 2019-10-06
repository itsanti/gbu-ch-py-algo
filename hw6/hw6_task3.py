"""HW6 - Task 3

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

import sys
from math import sqrt
from memory_profiler import profile

print(sys.version, sys.platform)


def meminfo(obj):
    print(f'ref count: {sys.getrefcount(obj)}')
    print(f'sizeof: {sys.getsizeof(obj)}')


@profile()
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
    meminfo(result)
    return result[n - 1]


@profile()
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
    meminfo(result)
    return result[n - 1]


n = 500
print(f"sieve: {sieve(n)}")
print(f"prime: {prime(n)}")


"""
3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] win32

Количество ссылок на объект result:
sieve: 6
prime: 6

Размер объекта result в байтах:
sieve: 4272 
prime: 7056 

Выделено памяти на выполнение скрипта:
sieve: 37.6 MiB
prime: 37.9 MiB

Вариант sieve - оптимальный по памяти.
"""
