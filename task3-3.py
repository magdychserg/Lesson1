#функция суммы двух наибольших чисел
def my_func(arg1, arg2, arg3):
    arg = [arg1, arg2, arg3]
    arg.remove(min(arg))
    return sum(arg)

print(my_func(3,23,4))
