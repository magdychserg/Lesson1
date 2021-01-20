#возведение в степень без встроенных функций
def my_func(arg1, arg2):
    return 1 / arg1 ** abs(arg2)

def my_func_for(arg1, arg2):
    res = 1
    for i in range(abs(arg2)):
        res *= arg1
    return 1/res

print(f'Answer through ** :', my_func (2, -3))
print(f'Answer through for :', my_func_for(2, -3))
