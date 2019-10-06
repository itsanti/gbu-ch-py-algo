"""HW6 - Task 1

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
def slice(a):
    meminfo(a[::-1])
    return a[::-1]


@profile()
def reverse(a):
    a = list(a)
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    meminfo(a)
    return "".join(a)


@profile()
def recursion(a):
    if len(a) == 1:
        meminfo(a)
        return a
    else:
        return a[-1] + recursion(a[:-1])


value = "3486"
print(f"slice: {slice(value)}")
print(f"reverse: {reverse(value)}")
print(f"recursion: {recursion(value)}")


"""
3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] win32

Количество ссылок на объект a:
slice: 4
reverse: 6
recursion: 72

Размер объекта a в байтах:
slice: 53 
reverse: 120 
recursion: 50

Выделено памяти на выполнение скрипта:
slice: 37.7 MiB
reverse: 37.7 MiB
recursion: 37.7 MiB

Вариант slice - оптимальный по памяти.
"""
