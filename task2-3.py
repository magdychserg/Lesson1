# Перевод месяца во время года с помощью словаря
seasons = {'Winter': (1, 2, 12),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Choose a month: '))
if month > 12 or month < 1:
    print('No this month')
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# Перевод месяца во время года с помощью списка
season = ['Winter', 'Spring', 'Summer', 'Autumn']
if month > 0 and month < 3 or month == 12:
    print(season[0])
elif month >2 and month < 6:
    print(season[1])
elif month > 5 and month < 9:
    print(season[2])
elif month > 8 and month < 12:
    print(season[3])
else:
    print('No this month')