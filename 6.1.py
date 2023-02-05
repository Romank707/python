import time

class TrafficLight:
    color_time = {'Красный': 7,
                   'Желтый': 2,
                   'Зеленый': 6}
    __color = None
    __c_index = 0
    # lighting = True
    change_count = 3

    def __init__(self, init_color='Зелёный', change_count=3):
        self.__color = init_color if self.color_time.get(init_color) else list(self.color_time.keys())[self.__c_index]
        self.__c_index = list(self.color_time.keys()).index(self.__color)
        self.change_count = change_count

    def running(self):
        print(self.__color)
        while self.change_count:
            time.sleep(self.color_time.get(self.__color))
            self.__c_index = (self.__c_index + 1) % 3
            self.__color = list(self.color_time.keys())[self.__c_index]
            print(self.__color)
            self.change_count -= 1


if __name__ == '__main__':
    while True:
        change_count = input('Сколько раз изменить цвет?')
        try:
            change_count = int(change_count)
            break
        except ValueError as e:
            print('Введите целое число')
    lights = TrafficLight('Красный', change_count)
    lights.running()







































