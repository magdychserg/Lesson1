#функция сдожения чисел
def my_func():
    res = 0
    while True:
        numbers =input('Enter list number through space or q for Exit: ').split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:#Если не число или q то ошибка и возврат к вводу
                print('It is not a number. Please enter number or q for Exit')
        print(f'Sum is {res}')

my_func()