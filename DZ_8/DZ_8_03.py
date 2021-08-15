class MyList(Exception):
    def __init__(self, text):
        self.txt = text


list = []
a = 0
while a != '!':
    a = input("Введите число: ")

    try:
        a = float(a)
        if a is False:
            raise MyList("Вы ввели не число !!!!")
    except ValueError:
        print("Ошибка типа значения! Вы ввели не число !!!")
    except MyList as ml:
        print(ml)
    else:
        list.append(a)
print(list)
