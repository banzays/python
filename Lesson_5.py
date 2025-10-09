f = open('file_name.txt', 'r') # по умолчанию r
# print(f.read())
for line in f:
    print(repr(line))
f.close()

f = open('file2.txt', 'w')
strings = ['Hello', 'World']
for string in strings:
    f.write(string + '\n')

with open('file_name.txt', 'r') as f:
    print(f.read())



try:
    with open('file_name.txt', 'r') as f:
        a = int(f.read())

except FileNotFoundError:
     print('Файл не найден')


except ValueError:
    print('Некорректное содержимое файла')
    raise ValueError

finally:
    print('Приложение завершено успешно')




