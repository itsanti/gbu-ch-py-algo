"""HW6 - Task 2

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

import sys
from memory_profiler import profile

print(sys.version, sys.platform)


def meminfo(obj):
    print(f'ref count: {sys.getrefcount(obj)}')
    print(f'sizeof: {sys.getsizeof(obj)}')


@profile()
def recursion(n):
    if n == 0:
        return 0
    return 1 + recursion(n - 1) / -2


@profile()
def cicle(n):
    a = 1
    i = 0
    summa = 0
    while i < n:
        summa += a
        a = a / -2
        i += 1
    meminfo(summa)
    return summa


n = 10
print(f"recursion: {recursion(n)}")
print(f"cicle: {cicle(n)}")


"""
3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] win32

Выделено памяти на выполнение скрипта:
recursion: 37.6 MiB
cicle: 37.6 MiB

Вариант cicle - оптимальный по памяти, т.к. не нужно выделять память в стеке под каждый рекурсивный вызов.
"""
