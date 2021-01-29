import json
with open('task5-7.txt', 'r', encoding='utf-8') as f:
    statistic = {}
    aver = {}
    stat = []
    k = 0
    n = 0
    average = 0
    for i in f:
        firm, forma_firm, revenue, cost = i.split()
        summa = int(revenue) - int(cost)
        if summa > 0:
            k += summa
            n += 1
        average = int(k/n)
        print(int(k/n))
        aver = {'average': average}
        statistic[firm] = summa

stat.append(statistic)
stat.append(aver)
print(stat)

with open('task5-7.json', 'w') as write_js:
    json.dump(stat, write_js)

    js_str = json.dumps(stat)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')