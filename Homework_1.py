# 1) Найти минимальное число в списке (можно создать любой список чисел)

numbers = []
# обрабатываем случай, если лист пуст
if numbers:

# через функцию min
    print('Минимальное число в списке через min: ', min(numbers))

# через перебор значений
    minNumber = numbers[0]
    for i in numbers:
        if i < minNumber:
            minNumber = i
    print('Минимальное число в списке через перебор: ', minNumber)

# Не понял как сделать тоже самое через list comprehension. Ругается на minNumber=i, но не понимаю как это написать по-другому
# print([minNumber=i for i in numbers if i < minNumber])


# 2) Посчитать количество цифр в строке (например в такой "Сегодня 05.09.2025") - в питоне есть метод для проверки на число isdigit() он тебе поможет)
text = "Сегодня 05.09.2025"
counter = 0
for char in text:
    if char.isdigit():
        counter += 1
print('Количество цифр в строке:', text, '= ', counter)


# 3) Вычислить факториал числа
x = int(input('Введите число: '))
f = 1
i = 1
while i <= x:
    f *= i
    i += 1
print('! ',x, '= ', f)