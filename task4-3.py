#Числа кратные 20 и 21 с помощью генератора
print(f'{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')