from functools import reduce

my_list = [i for i in range(100, 1001, 2)]

print("Список четных чисел от 100 до 1000:\n", my_list)
print("Произведение всех четных чисел списка:\n", reduce(lambda a, b: a * b, my_list))








































