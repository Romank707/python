from itertools import cycle

my_list = [1, 7, 3, 9, 5]

for i, j in enumerate(cycle(my_list)):
    print(j, end=' ')
    if i > 13:
        print()
        break









































