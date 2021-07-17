second = int(input("Введите время в секундах ?"))
ss = second % 60
mm = second // 60 % 60
hh = second // 3600
print(f"Получается {second} секунд составляет - {hh}.{mm}.{ss} чч.мм.сс.")
