in_list = [12, 13, -2, 0, 7, 453, 234, 34, 300, 2, 62, 544, 7, 740, 286, 40, 78, 234, 13, 286, 62]
new_list = [n for n in in_list if in_list.count(n) == 1]
print(new_list)
