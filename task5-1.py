#создание файла с вводом текста пользователем

with open("task5-1.txt", "w") as f:
    while True:
        line = input("Enter anything <ENTER FOR EXIT> : ")
        if line == '': break
        f.write(line + '\n')