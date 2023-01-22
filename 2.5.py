my_rating = [11, 10, 7, 4, 1, 1]
print(f"Текущий рейтинг: {my_rating}")

new_number = int(input("Введите новый элемент рейтинга: "))

for i in range(0, 1):
    if new_number >= 0:
        my_rating.append(new_number)
        my_rating.sort(reverse=True)
        print(f"Новый рейтинг: {my_rating}")
    else:
        print("Введено некорректное число")


































