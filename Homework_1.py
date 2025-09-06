# 1) Найти минимальное число в списке (можно создать любой список чисел)

listOfNumbers = [3,2,3,12,5,6,10, 1.2,]

# через функцию min
print('Минимальное число в списке через min: ', min(listOfNumbers))

# через перебор значений
minNumber = listOfNumbers[0]
for i in listOfNumbers:
    if i < minNumber:
        minNumber = i
print('Минимальное число в списке через перебор: ', minNumber)

# Не понял как сделать тоже самое через list comprehension. Ругается на minNumber=i, но не понимаю как это написать по-другому
# print([minNumber=i for i in listOfNumbers if i < minNumber])


# 2) Посчитать количество цифр в строке (например в такой "Сегодня 05.09.2025") - в питоне есть метод для проверки на число isdigit() он тебе поможет)
text = "Сегодня 05.09.2025"
counter = 0
for i in text:
    if i.isdigit():
          counter += 1
print('Количество цифр в строке:', text, '= ', counter)


# 3) Вычислить факториал числа
x = int(input('Введите число: '))
f = 1
i = 1
while i < x:
    f = f * (i+1)
    i += 1
print('! ',x, '= ', f)