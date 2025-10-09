import math, time

# 4) И замерь скорость их выполнения :)
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print(f'Время выполнения функции {func}: {finish_time - start_time} ')
        return result
    return wrapper

# 1) Напиши функцию calculate, которая принимает любое количество чисел и параметр operation. Если operation="sum",
# функция возвращает сумму всех чисел. Если operation="mul", функция возвращает их произведение.
@time_decorator
def calculate(operation, *numbers):
    if operation == 'sum':
        return print(f'Сумма всех чисел: {sum(numbers)}')
    elif operation == 'mul':
        return print(f'Произведение всех чисел: {math.prod(numbers)}')
    else:
        return print('Выберите операцию "sum" или "mul"')
calculate('sum', 1,2,3,4)


# 2) Напиши функцию update_dict, которая принимает словарь и любое количество именованных аргументов. Функция должна обновлять словарь значениями из kwargs и возвращать новый словарь.
@time_decorator
def update_dict(dicts, **kwargs):
    dicts.update(kwargs)
    return dicts

update_dict({'name':'Siroja', 'age':'31'}, nationality='Russian')

# 3) Напиши функцию filter_list, которая принимает список data и набор значений через *args. Функция должна возвращать новый список, в котором исключены все элементы из data, которые встречаются в args.
@time_decorator
def filter_list(data, *args):
    data = set(data)
    for i in args:
        if i in data:
            data.remove(i)
    return list(data)

print(filter_list([1,2,3,4,1,'apple'],'banana', 'apple', 1, 9, 8))

