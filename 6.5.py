class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print("\nРодительский метод класса Stationery")
        print("Запуск отрисовки\n")


class Pen(Stationery):
    def draw(self):
        print("Родительский метод класса Pen")
        print("Запуск отрисовки - ручка\n")


class Pencil(Stationery):
    def draw(self):
        print("Родительский метод класса Pencil")
        print("Запуск отрисовки - карандаш\n")


class Handle(Stationery):
    def draw(self):
        print("Родительский метод класса Handle")
        print("Запуск отрисовки - маркер")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()




















