a = int(input())
b = int(input())

i = 1

while a <= b + 1:
    print(f'{i}-й день:  {round(a, 2)}')
    if a > b:
        break
    a *= 1.1
    i += 1
print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км')





















