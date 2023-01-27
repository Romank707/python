def sum_number ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа или r для выхода- ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'r' or number[el] == 'R':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Итоговая сумма: {sum_res}')
sum_number()





































