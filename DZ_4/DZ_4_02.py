in_list = [12, 13, -2, 0, 453, 234, 34, 300, 2, 62, 544, 7, 740, 287, 40, 78]
good_list = [in_list[i] for i in range(1, len(in_list)) if in_list[i] > in_list[i-1]]
print(good_list)
