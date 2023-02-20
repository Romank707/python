def currency_exchange(usd):
    ref1 = usd / 1.17
    return ref1


usd = float(input("Введите необходимую сумму в долларах США: "))

print("Сумма перевода в Euro составит = ", '{:.2f}'.format(currency_exchange(usd)))

