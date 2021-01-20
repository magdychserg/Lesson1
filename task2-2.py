#Замена введеных символов местами. 1 и 2 , 3 и 4 и т.д.
spisok = list(input('Введите символы для создания списка: '))#создание списка
print(f"Your list:", spisok)
for i in range(1, len(spisok), 2):
    spisok[i-1], spisok[i] = spisok[i], spisok[i-1]
print(f"New list:", spisok)
