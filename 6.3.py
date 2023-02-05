class Worker:

    def __init__(self, name='Иван', surname='Пушной', position='дворник', wage=1000, bonus=200):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_worker = Position('Андрей', 'Ворошилов', 'преподаватель', 1500, 300)
print(f'Новый атрибут: {v_worker.name}, {v_worker.surname}, {v_worker.position}, {v_worker._income}')
print(f'Полная зарплата {v_worker.get_full_name()} составляет {v_worker.get_full_salary()}')










































