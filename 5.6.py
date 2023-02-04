import re

report = {}
with open('task06.data.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    for row in file:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        report.update({row_items[0]: sum([int(i) for i in hours])})

print(f"Исходный файл:\n{text}\n")
print(f"Словарь:\n{report}")








































