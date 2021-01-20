#вывод слов с первой заглавной.
# Смысл 7 задачи если эта функция это тоже делает и со словами через пробел
def int_func(text):
    return text.title()

print(int_func('hy my teacher'))

#Вариант только для одного слова
def int_func_one(text):
    if text:
        return text[0].upper() + text[1:]
    return text[:]
print(int_func_one('hello'))

##Перевод в заглавные через ord
def int_func_ord(text):
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].replace(words[i][0], chr(ord(words[i][0]) - 32))
    return ' '.join(words)

print(int_func_ord('i love python'))

#решение задачки с помощью ранее созданной функции int_func_one
def int_func_multi(text):
    a = text.split()
    res = []
    for text in a:
       res.append(int_func_one(text))
    return ' '.join(res)
print(int_func_multi('hello kamchatka'))
