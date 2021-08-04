translat = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре"
    }
with open('Text_5_04.txt') as file, open('Text_5_14.txt', 'w') as new_file:
    line_st = file.readlines()
    for el in line_st:
        trans_info = el.split()
        rus_trans = translat.get(trans_info[0])
        new_file.write(f'{trans_info[0], rus_trans}')
