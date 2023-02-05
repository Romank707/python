class Car():

    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed # максимальная скорость
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новый автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed  > self.max_speed and not self.is_police:
            print('Превышена разрешенная скорость!')

    def go(self):
        print(f'{self.name} начала движение')

    def stop(self):
        print(f'{self.name} совершила остановку')

    def turn(self, direction):
        print(f'{self.name} свернула {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Семейный автомобиль')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Спортивный автомобиль')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Служебный автомобиль')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Полицейский автомобиль')


family_car = TownCar(60, 'белый', 'Кия Рио', False)
family_car.go()
family_car.show_speed(40)
family_car.show_speed(50)
family_car.show_speed(60)
family_car.turn('направо')
family_car.turn('налево')
family_car.stop()
print()

work_car = WorkCar(60, 'красный', 'Шкода бусик', False)
work_car.go()
work_car.show_speed(40)
work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Тойота', True)
print()

sport_car = SportCar(60, 'желтый', 'феррари', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
sport_car.stop()











































