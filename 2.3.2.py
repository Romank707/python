# решение задачи 2.3 с применением list

list_month = [['Зима', 12, 1, 2],
              ['Весна', 3, 4, 5],
              ['Лето', 6, 7, 8],
              ['Осень', 9, 10, 11]]

month_number = int(input('Введите номер месяца: '))

if month_number in range(1, 13):
    for i, elem in enumerate(list_month):
        if month_number in elem[1:4]:
            print(f'{elem[0]}')
            break
else:
    print('Введен некорректный номер')
































