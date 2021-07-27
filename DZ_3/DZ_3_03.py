def my_funk (v, n, m):
    resultat = v + n + m - min(v, n, m)
    return resultat
input_data = str(input('введите 3 числа через пробел'))
in_data = input_data.split()
print(in_data)
a = float(in_data[1])
b = float(in_data[2])
c = float(in_data[0])
print(my_funk(a, b, c))
