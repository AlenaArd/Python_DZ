from itertools import cycle, count

abc_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
num_list = [n for n in range(11, 80, 11)]
print (num_list)
n = 17

new_abc = [cycle(abc_list)]
print(new_abc[:18])

#abc_list = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg']
