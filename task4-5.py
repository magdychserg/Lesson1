#Перемножение всех четных чисел от 100 до 1000
from functools import reduce

def my_func(el_prev, el):
    return el_prev * el

print(reduce(my_func,[el for el in range(100, 1001, 2)]))


