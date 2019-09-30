"""HW3 - Task 1

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple, deque

Company = namedtuple('Company', ['name', 'q1', 'q2', 'q3', 'q4', 'profit'])
sum_year = 0
companies = []

num = int(input("Введите количество предприятий: "))
for i in range(num):
    name = input(f"Введите название предприятия #{i + 1}: ")
    q1, q2, q3, q4 = map(int, input(f"Введите прибыль предприятия 'q1 q2 q3 q4': ").split())
    loc_sum = sum([q1, q2, q3, q4])
    sum_year += loc_sum
    companies.append(Company(name, q1, q2, q3, q4, loc_sum))

avg_profit = sum_year / num

deque_comp = deque([None])
for company in companies:
    if company.profit > avg_profit:
        deque_comp.appendleft(company)
    elif company.profit < avg_profit:
        deque_comp.append(company)

print(f"Средняя прибыль за год для всех предприятий: {avg_profit:.2f}")

msg = 'выше'
for company in deque_comp:
    if company is None:
        msg = 'ниже'
        continue
    print(f"Прибыль {company.name} {msg} средней: {company.profit}")

'''
Введите количество предприятий: 3
Введите название предприятия #1: 1
Введите прибыль предприятия 'q1 q2 q3 q4': 1 2 3 4
Введите название предприятия #2: 2
Введите прибыль предприятия 'q1 q2 q3 q4': 2 3 4 5
Введите название предприятия #3: 3
Введите прибыль предприятия 'q1 q2 q3 q4': 3 4 5 6
Средняя прибыль за год для всех предприятий: 14.00
Прибыль 3 выше средней: 18
Прибыль 1 ниже средней: 10
'''
