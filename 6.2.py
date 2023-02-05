class Road():


    __weight = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight / 1000

        return ret_val

r = Road(5000, 20)
w = r.get_weight(5)

print(f'Вес асфальта = {round(w)} т.')








































