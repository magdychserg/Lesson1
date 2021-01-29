#Подсчет количества строк и слов в файле
with open('task5-1.txt', 'r') as f:
    data = f.readlines()
print(f'Number of lines in the file  - {len(data)}')

with open('task5-1.txt', 'r') as f:
    data_word = f.read()
    data_word = data_word.split()
print(f'Number of words in the file - {len(data_word)}')
