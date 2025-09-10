# Дз. Ознакомься с этой докой, и попробуй поискать в ней нужные тебе методы для решения дз https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

# 1)# У тебя есть строка с паролем " Py1234 "
# # Убери лишние пробелы.
# # Если длина пароля меньше 8 символов — выведи "Пароль слишком короткий".
# # Если пароль содержит хотя бы одну цифру — выведи "Пароль содержит цифры".
# # Сделай пароль полностью заглавными буквами и выведи результат.

password = input('Введите пароль:')
# password = (password.replace(' ', ''))
password = password.strip()
digit = False
for char in password:
    if char.isdigit():
        digit = True

if digit:
    print('Пароль содержит цифры')
elif len(password) < 7:
    print('Пароль слишком короткий')
else:
    print(password.upper())

# 2)
# Есть строка "20250908"
# Используя срезы, извлеки день, месяц и год.
# Если день < 10 — добавь ведущий ноль.
# Выведи дату в формате "DD.MM.YYYY".

date = '2025098'
year = date[:4:]
month = date[4:6]
day = date[6:8]

if len(day) < 2:
    day = '0' + day

print(f'{day}.{month}.{year}')


#
# 3)
# Есть строка: "Python is fun and Python is powerful"
# Раздели строку на слова.
# Посчитайте, сколько раз встречается слово "Python".
# Если количество больше 1 — выведите "Python встречается часто", иначе "Python встречается редко".

string = "Python is fun and Python is python powerful"
count_of_Python = 0
for word in (string.split(' ')):
    if word == 'Python' or word == 'python':
        count_of_Python += 1
if count_of_Python > 1:
    print('Python встречается часто')
else:
    print('Python встречается редко')






