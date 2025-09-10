# Неизменяемые типы данных
# Кортеж
# Строка
# Целочисленный
# С плавающей точкой
# Bool
# None
# Frozen set


# Изменяемые типы данных
# Списки
# Множество
# Словари


# Целые числа:
x = 10
print(x / 10) # деление
print(x // 10) # деление без остатка
print(x % 10) # остаток от деления
print(x ** 10) # возведение в степень

print(round(x / 23, 2))
x = 10
# Логический тип
if x:
    print('Число положительное')
else:
    print('Число неположительное')


# Строки:
s = 'Hello'
print(id(s))
print(id(s))
print(s)
s2 = 'World'

print(s + '' + s2)
print('{a} {b}'.format(a=s,b=s2)) # старый формат
print(f'{s} {s2} {s2*2}')
print(s.upper())
print(s.lower())
print(s.split('l'))
print(s.replace('H', 'Q'))
print(s[::-1]) # отрицательный шаг для переворота строки

