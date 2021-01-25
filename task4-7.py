#Вычесление факториала без вызова встроенной функции с помощью yield
def fact(n):
    x = 1
    for el in range(1, n + 1):
        x *= el
        print(f'{el}! - {x}')
        yield x


n = 15
factorial = [el for el in fact(n)]

