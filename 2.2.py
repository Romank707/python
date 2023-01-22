my_list = list(input("Введите элементы: "))
# элементы вводятся без пробелов

a = my_list

for i in range(0, len(a)-1, 2):
    a[i], a[i+1] = a[i+1], a[i]

print(a)
































