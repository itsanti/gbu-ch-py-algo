"""HW5 - Task 2

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

не использовать встроенные hex() и/или int()
"""

from collections import deque

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

HEX_DEC_MAP = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

first = deque(input('Введите первое x16 число: ').upper())
second = deque(input('Введите второе x16 число: ').upper())


def hex_sum(a, b):
    a = a.copy()
    b = b.copy()
    if len(a) < len(b):
        a, b = b, a

    result = deque()
    offset = 0
    while len(b):
        s = HEX_DEC_MAP[a.pop()] + HEX_DEC_MAP[b.pop()] + offset
        offset = 1 if s // 16 > 0 else 0
        result.appendleft(HEX_NUMBERS[s % 16])
    if offset > 0:
        while offset > 0 and len(a):
            s = HEX_DEC_MAP[a.pop()] + offset
            offset = 1 if s // 16 > 0 else 0
            result.appendleft(HEX_NUMBERS[s % 16])
        if offset:
            result.appendleft(HEX_NUMBERS[offset])
    return a + result


def hex_mul(a, b):
    result = deque()
    a = a.copy()
    b = b.copy()
    if len(a) < len(b):
        a, b = b, a

    shift = 0
    while len(b):
        _result = deque()
        _b = b.pop()
        offset = 0

        _a = a.copy()
        while len(_a):
            s = HEX_DEC_MAP[_a.pop()] * HEX_DEC_MAP[_b] + offset
            offset = s // 16 if s // 16 > 0 else 0
            _result.appendleft(HEX_NUMBERS[s % 16])
        if offset > 0:
            _result.appendleft(HEX_NUMBERS[offset])

        if len(result) == 0:
            result = _result
        else:
            shift += 1
            _result.extend([HEX_NUMBERS[0]] * shift)
            result = hex_sum(result, _result)
    return result


print(f'first: {first}\nsecond: {second}')
print(f'sum: {hex_sum(first, second)}')
print(f'mul: {hex_mul(first, second)}')

'''
first: deque(['A', '2'])
second: deque(['C', '4', 'F'])
sum: deque(['C', 'F', '1'])
mul: deque(['7', 'C', '9', 'F', 'E'])

first: deque(['A', 'B', 'C', '4', '5', '6'])
second: deque(['D', 'F', '6', '7'])
sum: deque(['A', 'C', 'A', '3', 'B', 'D'])
mul: deque(['9', '5', 'E', '5', '2', '2', 'E', '8', '9', 'A'])
'''
