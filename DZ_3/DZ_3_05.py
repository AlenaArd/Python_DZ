
def sum_num(num_same, br):
    good_list = num_same.split(' ')
    sum_list = 0
    for i in good_list:
        if i == br:
            break
        sum_list += int(i)

    return sum_list


br = '!'
stp = False
s = 0
while not stp:
    num_same = input('введите несколько чисел через пробел, "!" закончит действие программы')
    s += sum_num(num_same, br)
    if br in num_same:
        break
    print(f'Сумма всех чисел = {s}')
