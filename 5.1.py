my_file = open('poem.txt', 'w')
line = input('Введите текст \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
my_f = open('poem.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()






































