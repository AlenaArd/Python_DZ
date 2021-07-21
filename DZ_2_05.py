rating = [11, 9, 9, 8, 6, 6]
qt_el = int(input('Введите колличество новых эементов рейтинга'))
q = 1
while q <= qt_el:
    new_el = int(input('Введите новый эемент рейтинга - натуральное число'))
    i = len(rating)
    while i > 0:
        if new_el <= rating[i - 1]:
            rating.insert(i, new_el)
            print(rating)
            break
        else:
            i -= 1
    q += 1
print('рейтинг готов')
