# Создать базовый класс Vehicle (транспортное средство), который должен содержать:
# приватные атрибуты _brand (марка) и _speed (скорость);
# свойство brand: доступно только для чтения (read-only, без setter), изменить марку после создания объекта нельзя;
# свойство speed: доступно для чтения и изменения, при установке (setter) не допускает отрицательных значений, при попытке задать отрицательное значение выбрасывает ValueError.
# метод get_info() для вывода общей информации о транспорте.
#
#
# Создать классы-наследники:
# Car — дополнительно имеет поле seats (количество мест),
# Bus — дополнительно имеет поле capacity (вместимость пассажиров),
# Bike — дополнительно имеет поле bike_type (например, "горный" или "шоссейный").
#
# В каждом из этих классов переопределить метод get_info(), чтобы он выводил общие данные из базового класса и свои специфические данные.
#
# Добавить метод trip_cost(distance) в каждый класс:
# Для Car стоимость рассчитывается как distance * 0.1. Для Bus — distance * 0.05 * capacity. Для Bike — 0 (поездка бесплатная).
#
# Создать список из объектов разных классов (Car, Bus, Bike) и в цикле:
# вывести их информацию через метод get_info(),
# посчитать стоимость поездки на дистанцию, например, 100 км.



class Vehicle:
    def __init__(self, brand, speed):
       self._brand = brand
       self._speed = speed

    @property
    def brand(self):
        return self._brand

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError('Скорость не может быть отрицательной')
        else:
            self._speed = speed

    def get_info(self):
        return f'Бренд: {self.brand}, Скорость: {self.speed}'


class Car(Vehicle):
    def __init__(self, brand, speed, seats):
        self.seats = seats
        super().__init__(brand, speed)

    def get_info(self):
        return f'Бренд: {self.brand}\nСкорость: {self.speed}\nКоличество мест: {self.seats}'

    @staticmethod
    def trip_cost(distance):
        return f'Стоимость поездки: {distance * 0.1}\n'


class Bus(Vehicle):
    def __init__(self, brand, speed, capacity):
        self.capacity = capacity
        super().__init__(brand, speed)


    def trip_cost(self,distance):
        return f'Стоимость поездки: {distance * 0.05 * self.capacity}\n'

    def get_info(self):
        return f'Бренд: {self.brand}\nСкорость: {self.speed}\nВместимость пассажиров: {self.capacity}'


class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        self.bike_type = bike_type
        super().__init__(brand, speed)

    @staticmethod
    def trip_cost(distance):
        return f'Стоимость поездки: 0\n'

    def get_info(self):
        return f'Бренд: {self.brand}\nСкорость: {self.speed}\nТип байка: {self.bike_type}'

niva = Car('Нива', 70, 6)
lada = Car('Lexus', 90, 5)
bus = Bus('Мерседес', 50, 30)
bike = Bike('BMX', 20, 'Горный')

vehicle_list = [
    Car('Нива', 70, 6),
    Car('Lexus', 90, 5),
    Bus('Мерседес', 50, 30),
    Bike('BMX', 20, 'Горный')
]

for vehicle in vehicle_list:
   print(vehicle.get_info())
   print(vehicle.trip_cost(100))
