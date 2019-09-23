"""HW2 - Task 5

Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

i = 1
for code in range(32, 128):
    end = '\n' if i % 10 == 0 else '\t'
    print(f'{code:3}-{chr(code)}', end=end)
    i += 1