# Поиск максимальой цифры в введеном числе
number = int(input("Enter an integer: "))
number_max = number%10 #получаем последнюю цифру
number = number//10 #уменьшаем введеное число на один знак
while number > 0:
    if number%10 > number_max:
        number_max = number%10
    number = number//10
print(f"Max figure your numder: ", number_max)