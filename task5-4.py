#перевод слов и замена их в тексте
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('task5-4.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(translate[i[0]] + '  ' + i[1])

with open('task5-4_new.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_file)