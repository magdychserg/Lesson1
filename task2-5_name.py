#Рейтинг с именами
place = int(input('Enter place: '))
name = input('Enter name players: ')
my_list = {'Olga': 7, 'Petr': 2, 'Don': 4, 'Svetlana': 3}
my_list[name] = place
for i, (k, v) in enumerate(sorted(my_list.items(), key= lambda n: n[1]), 1):
    print(f'{v} - {k}')