# Перевод введеных секунд в часы, минуты и секунды
time = int(input("Enter the time in seconds: "))
hour = time // 3600
minute = (time // 60) % 60
seconds = time % 60
print(f"Your time ", hour,"h ", minute,"m ", seconds, "s")