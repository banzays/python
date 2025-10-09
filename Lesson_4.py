import time

def hello(name):
   return f'Hello, {name}'

result = hello('Sergei')
print(result)

def summary(number_1, number_2):
    return number_1 + number_2

print(summary(1, 2))
print(summary(number_2=2, number_1=1))

def summary2(*number):
    return sum(number)


print(summary2(1, 2, 3 ,4))

def print_scores(student, *scores):
    print(student)
    for score in scores:
        print(score)

print_scores('Iurchenko', 2,3,4)

def print_scores2(student, **scores):
    print(student)
    for subject, score in scores.items():
        print(f' {subject}: {score}')

print_scores2('Iurchenko', math=2, russian=3, python=1)
print_scores2('Ivanov', english=2, js=3)

def get_settings(**settings):
    cpu = settings.get('cpu', 2000)
    ram = settings.get('ram', 256)
    cores = settings.get('cores', 1)
    print(f'Приложение запущено с параметрами: cpu = {cpu}, ram = {ram}, cores = {cores}')

get_settings(cpu= 2000, ram=1024, cores=2)

get_settings()

summary3 = lambda x: x**3
get_settings(cpu=summary3(10))
summary3(10)


numbers = [1, 2, 3, 4 ,5]
square = map(lambda x: x**2, numbers)
print(list(square))

def null_decorator(func):
    print('Я декоратор')
    return func

def great():
    return 'Hello'

greet = null_decorator(great)
print(greet())

@null_decorator
def great():
    return 'Hello'

print(great())

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        finish_time = time.time()
        return result

    return wrapper()
