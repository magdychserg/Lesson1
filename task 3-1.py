#создание функции деления двух аргументов
def arg(arg1, arg2):
    try:
        arg1 / arg2
    except ZeroDivisionError:
        return print('Division by zero')
    res = arg1 / arg2
    return res

print(arg((int(input('Enter arg1: '))), (int(input('Enter arg2: ')))))
