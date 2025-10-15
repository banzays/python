from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figura):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        pass
    def area(self):
        pass

circle = Circle(20)

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        print(f'Создано животное с именем {name}, и возрастом {age}')

    @property
    def age(self):
       return f'Возраст животного: {self._age}'

    @age.setter
    def age(self, age):
        if self._age <= age:
            self._age = age
        else:
            raise ValueError('Возраст не может быть меньше текущего')




animal = Animal(name='Bobik', age=20)
animal.age = 21
print(f'{animal.age}  1231231')

class Dog(Animal):
    def __init__(self, name, age, breed = None):
        self.breed = breed
        super().__init__(name, age)

    def introduce(self):
        print(f'Животное - собака, порода = {self.breed}')


dog = Dog(name = 'Pushok', age = 45, breed = 'Ovcharka')
dog.age = 50
print(dog._age)

class Cat(Animal):
    def __init__(self, name, age, breed = None):
        self.breed = breed
        super().__init__(name, age)

    def introduce(self):
        print(f'Животное - кошка, порода = {self.breed}')

cat = Cat(name = 'Кошка', age='45', breed='Siamskaya')

for animal in dog,cat:
    print(animal.introduce())

class Helper():
    @staticmethod
    def plus():
        pass
    @staticmethod
    def minus():
        pass

Helper.plus()

a = [1, 2, 3]
print(len(a))
