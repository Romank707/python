class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Результат сложения клеток: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Результат вычитания: {sub}' if sub > 0 else 'Результат вычитания: Клетка исчезла'

    def __truediv__(self, other):
        return f'Результат деления клеток: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Результат умножения клеток: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(15)
cell_2 = Cell(3)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))
