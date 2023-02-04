f = open('file_task_05.txt', 'w')
print("Введите числа, разделенные пробелами: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break

f = open('file_task_05.txt', 'r')
list = f.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()








































