"""HW9 - Task 1

Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
"""

import hashlib


def substring_count(string):
    sub_strings = set()
    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            if string == string[i:j]:
                continue
            sub = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sub_strings.add(sub)
    return len(sub_strings)


print(substring_count('papa'))
print(substring_count('sova'))
