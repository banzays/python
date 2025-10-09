import copy

# Кортежи
a = (1, False , 'string', (1, 2, 3)) # Можно писать и без скобок и даже только с запятой
print(a[3][1])
print(a.count(1))


# Списки
a = [1, False , 'string', (1, 2, 3)]
b = [1, 2, 3, (1,2,3)]
c = b.copy()
d = copy.deepcopy(b)
print(a[3][1])
print(a.count(1))
print(a.append('string2'))
print(a)


b.append(4)
print(c)
print(b)

print(d)

# Set
a = (1, 2, 3, 4, 1)
print(tuple(set(a)))
b = 'strings123'
print(list(b))


# Словари

a = {'name': 'Sergei', 'lastname': 'Iurchenko'}
print(a['name'])
a['name'] = 'Ivan'
print(a)
a['age'] = 31

a.update({'name': 'Sergei'})
print(a)
print(a.get('adress', 'Адресс отсутствует'))

print(list(a.keys()))
print(a.values())
print(a.items())

# Циклы

for k, v in a.items():
    print(k)
    print(v)


people = [{'name': 'Sergei', 'lastname': 'Iurchenko'}, {'name': 'Ivan'}, {'name': 'John', 'lastname': 'Dhoe'}]

for i in people:
    print(i)
    for k,v in i.items():
        print(k)
        print(v)

for i in people:
    print(i)
    for k in i:
        lastname = i.get('lastname')

print('___________')

for i in people:
    if len(i) < 2:
        continue
    print(i)

i = 0
while True:
    print(i)
    if i == 10:
        break
    i+= 1

i = 0
while i <= 10:
    print(i)
    i+= 1

while True:
    i = int(input('Введите че нибудь'))
    if i == 1:
        break