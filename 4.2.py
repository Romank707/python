my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вариант 1

less_list = [num1 for num1, num2 in zip(my_list[1:], my_list[:-1]) if num1 > num2]

# вариант 2 c enumerate

less_list = [number for i, number in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]

print(less_list)








































