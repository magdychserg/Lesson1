# Выводим слова построчно если больше 10 выводим только 10
words = str(input('Enter words separated by a space ')).split()
a = 0
for i in words:
    a +=1
    if len(i) > 10:
        print(a, i[:10])
    else:
        print(a, i)


