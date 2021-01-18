#Замена введеных символов местами. 1 и 2 , 3 и 4 и т.д.
j = 0
spisok = list(input('Введите символы для создания списка: '))#создание списка
print(f"Your list:", spisok)
for i in range(int(len(spisok) / 2)):
    spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
    j += 2
print(f"New list:", spisok)
