# ДЗ : Еще раз пробежаться по методам списков https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html и словарей https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html

# 1) Подсчитать, сколько раз встречается каждое слово в списке,
#  и сохранить их в переменную. words = ["apple", "banana", "apple", "orange", "banana", "apple"]
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
dict_of_words = dict.fromkeys(words, 0)
list_of_words = []
for word in words:
    if word in list_of_words:
        dict_of_words[word] += 1
    else:
        list_of_words.append(word)
        dict_of_words[word] += 1
print(dict_of_words)

# 2) Собрать уникальные числа из матрицы и сохранить их в переменную. matrix = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
matrix = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
a = set()
for n in matrix:
    for i in n:
        a.add(i)
print(a)

# 3) Для каждой строки посчитать длину и количество слов,
# и сохранить их в переменную phrases = ["Hello World", "Python is fun", "I like coding", "Python is powerful"]
phrases = ["Hello World", "Python is fun", "I like coding", "Python is powerful"]
for string in phrases:
    length = len(string)
    words_count = len(string.split())

    print(f'Phrase: {string} \n Length: {length}; \n Words count: {words_count};')

    # В третьем задании хотел зафиксировать значения в виде ключ:значение, но не догнал как это сделать.
    # Пытался через update, но таким образом я сохраняю только данные из последней итерации
    # d.update({'phrase': string,'length': length, 'Words Count': words_count})





