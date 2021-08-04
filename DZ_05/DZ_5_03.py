with open('Text_5_03.txt') as file:
    line_st = file.readlines()
    salary_list = {}
    sum_salary = 0.0
    for el in line_st:
        salary_info = el.split()
        salary_list.update({salary_info[0]: float(salary_info[1])})
        sum_salary += float(salary_info[1])
average_sal = sum_salary / len(salary_list)
print(f'Средняя зарплата: {average_sal}')
salary_good = {}
salary_low = {}
for name, sal_n in salary_list.items():
    if sal_n > average_sal:
        salary_good.update({name: sal_n})
    else:
        salary_low.update({name: sal_n})
print(f'зарплата более 20 тыс.: {salary_good}')
print(f'зарплата более 20 тыс.: {salary_low}')
