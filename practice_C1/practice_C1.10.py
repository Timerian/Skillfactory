class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} рублей.'

    def get_info(self):
        return f'{self.name} {self.surname}. {self.city}.'


cl_1 = Clients('Вася', 'Пупкин', 'Усть-пиздюйск', -1000)

print(cl_1)
print(cl_1.get_info())

