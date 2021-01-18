#Добавление места в рейтинг
number = int(input("Enter number: "))
my_list = [8, 5, 3, 3, 2]
a = my_list.count(number)
for el in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    elif number > el:
        my_list.insert(my_list.index(el), number)
        break
    elif number < my_list[len(my_list) - 1]:
        my_list.append(number)
print(my_list)