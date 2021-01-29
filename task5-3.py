#вывод имен с окладом менее 20000 из файла
with open('task5-3.txt', 'r') as f:
    my_list = f.read().split('\n')
    salary_less = []
    salary = []
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            salary_less.append(i[0])
        salary.append(i[1])
print(f'The salary is less 20.000 {salary_less}, average salary {int(sum(map(int, salary)) / len(salary))}')
