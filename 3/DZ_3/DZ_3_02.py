def personal_list(name, surname, year, citi, email, tel):
    return (f'{name}, {surname}, {year}, {citi}, {email}, {tel}')


n = input('Имя:')
s = input('Фамилия:')
y = input('Год рождения:')
c = input('Город проживания:')
e = input('email:')
t = input('телефон:')
print(personal_list(n, s, y, c, e, t))
