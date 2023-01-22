# решение задачи 2.3 с использованием dict
seasons = dict(Зима= (1, 2, 12),
            Весна= (3, 4, 5),
            Лето= (6, 7, 8),
            Осень= (9, 10, 11))

month_number = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if month_number in seasons[key]:
        print(key)


































