# Выводим слова построчно если больше 10 выводим только 10
words = str(input('Enter words separated by a space ')).split()
for i, word in enumerate(words):
    print(i, word[:10])
