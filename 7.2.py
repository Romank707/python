from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Суммарный расход ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Something vary abstract'


class Coat(Clothes):
    def consumption(self):
        return f'Для изготовления пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Something vary abstract second'


class Costume(Clothes):
    def consumption(self):
        return f'Для изготовления костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass



coat = Coat(400)
costume = Costume(55)
print(coat.consumption())
print(costume.consumption())
print(coat.abstract())



