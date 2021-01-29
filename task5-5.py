with open('task5-5.txt', 'w', encoding='utf-8') as f:
    number = input('Enter number through space: ')
    f.write(number)

with open('task5-5.txt', 'r', encoding='utf-8') as f:
    try:
        print(f'The sum is equal to: {sum(map(int, f.read().split()))}')
    except:
        print('You enter not number')


