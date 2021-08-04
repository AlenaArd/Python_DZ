import json


compani_s = {}
compani_g = {}
compani_b = {}
compani_aver = {}
result_count = 0
result_sum = 0
with open('Text_5_07.txt') as file:
    compani_info = file.readlines()
    for info in compani_info:
        info_com = info.split()
        result_i = float(info_com[2]) - float(info_com[3])
        if result_i > 0:
            compani_g.update({info_com[0]: result_i})
            result_count += 1
            result_sum += result_i
        else:
            compani_b.update({info_com[0]: result_i})
print(f'Вот список убыточных компаний: {compani_b}')
print(f'Вот список компаний c прибылью: {compani_g}')
average_result = round(result_sum / result_count, 2)
print(f'успешных компаний: {result_count}, средняя прибыль для них: {average_result}')
result = [f'Successful companies:  {result_count}. Name : {compani_g}. Average profit {average_result}']


with open('Text_5_07.json', 'w') as file:
    json.dump(result, file)
