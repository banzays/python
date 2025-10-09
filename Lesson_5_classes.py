class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Создано животное с именем {name}, и возрастом {age}')

    def set_age(self, age):
        self.age = age



animal = Animal(name='Bobik', age='20')
animal.set_age(21)
print(animal.age)

class Dog(Animal):
    def __init__(self, name, age, breed = None):
        self.breed = breed
        super().__init__(name, age)
        print(f'Животное - собака, порода = {breed}')


dog = Dog(name = 'Pushok', age = '45', breed = 'Ovcharka')
dog.set_age(50)
print(dog.age)