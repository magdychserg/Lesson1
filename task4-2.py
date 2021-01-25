# Поиск числа большего предыдущего с помощью генератора
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list_new = [el for el in my_list if el > my_list[my_list.index(el)-1]]

print(my_list_new)