class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Enter the values and click Enter - '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Invalid value")
                y_or_n = input(f'Try again? Y - yes')
                if y_or_n == 'Y':
                    print(try_except.my_input())
                else:
                    return f'You are exit'

try_except = Error(1)
print(try_except.my_input())