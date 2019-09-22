"""HW1 - Task 5

Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

n = int(input("Введите номер буквы в алфавите [1-26]:"))

if n < 1 or n > 26:
    print("В алфавите нет буквы с таким номером.")
elif n == 1:
    print("Буква:", "a")
elif n == 2:
    print("Буква:", "b")
elif n == 3:
    print("Буква:", "c")
elif n == 4:
    print("Буква:", "d")
elif n == 5:
    print("Буква:", "e")
elif n == 6:
    print("Буква:", "f")
elif n == 7:
    print("Буква:", "g")
elif n == 8:
    print("Буква:", "h")
elif n == 9:
    print("Буква:", "i")
elif n == 10:
    print("Буква:", "g")
elif n == 11:
    print("Буква:", "k")
elif n == 12:
    print("Буква:", "l")
elif n == 13:
    print("Буква:", "m")
elif n == 14:
    print("Буква:", "n")
elif n == 15:
    print("Буква:", "o")
elif n == 16:
    print("Буква:", "p")
elif n == 17:
    print("Буква:", "q")
elif n == 18:
    print("Буква:", "r")
elif n == 19:
    print("Буква:", "s")
elif n == 20:
    print("Буква:", "t")
elif n == 21:
    print("Буква:", "u")
elif n == 22:
    print("Буква:", "v")
elif n == 23:
    print("Буква:", "w")
elif n == 24:
    print("Буква:", "x")
elif n == 25:
    print("Буква:", "y")
else:
    print("Буква:", "z")

# вариант короче
n = ord('a') + n - 1
print(f'Это буква {chr(n)}')