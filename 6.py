revenue = int(input())
costs = int(input())

r = revenue
d = costs
profit = r - d
p = profit
profitability = p / r
pr = profitability

if r > d:
    print(f'Рентабельность: {pr}')
    workers = int(input('Укажите количество работников: '))
    print(f' Прибыль фирмы в расчете на одного работника: {p / workers}')


















