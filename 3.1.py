def division(a, b):
    try:
        return a/b
    except ZeroDivisionError as elm:
        print(f'Делить на ноль нельзя')

print(division(int(input('Первое число: ')), int(input('Второе число: '))))








































