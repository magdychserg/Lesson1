# два скрипта, первый выводит целые числа, второй выводит элементы списка n раз
from itertools import count, cycle
import time

def my_func_count(start, stop):
    for el in count(start):
        if el > stop:
            break
        time.sleep(1)
        print(el)

def my_func_cycle(my_list, repetition):

    s = 1
    for i in cycle(my_list):
        if s > int(repetition):
            break
        s += 1
        print(f'{i}')
        time.sleep(1)

my_func_count(start = 3, stop = 10)
my_func_cycle(my_list =['Hy', 'friend', 2, 888], repetition =int(input('Enter the number of repetitions: ')))