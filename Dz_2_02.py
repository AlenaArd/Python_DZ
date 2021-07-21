one_str = input('Введите элементы списка через пробел, мы в нем поменяем соседние элементы местами.')
one_list = one_str.split()
new_list = []
i = 0
while i < len(one_list):
    d = one_list[i:i+2]
    d.reverse()
    new_list = new_list + d
    i += 2
else:
    print(new_list)
