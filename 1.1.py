first_name = input("Введите Ваше имя: ")
middle_name = input("Введите Ваше отчество: ")
last_name = input("Введите Вашу фамилию: ")

b = last_name + first_name + middle_name

for i in range(len(b)):
   print(b[i])
