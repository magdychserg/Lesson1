import re

with open('task5-6.txt', 'r', encoding='utf-8') as f:
    lesson = {}
    for i in f:
        subject, lecture, practic, lab = i.split()
        nums = [int(i) for i in re.findall(r'\b\d+\b', i)]
        lesson[subject] = sum(nums)
        print(f'{subject} - {sum(nums)} часов')
print(f'{lesson}')