def my_func(a, b, d):

    if a > b and b > d:
        s = a + b
    elif a < b and b < d:
        s = b + d
    elif a > b and b < d:
        s = a + d

    return s

print(my_func(int(input('Первое число: ')), int(input('Второе число: ')), int(input('Третье число: '))))








































