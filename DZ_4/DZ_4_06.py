from itertools import cycle, count

abc_list = [('Aa'), ('Bb'), ('Cc'), ('Dd'), ('Ee'), ('Ff'), ('Gg')]
num_list = [n for n in range(3, 11, 1)]
print(num_list)
n = 25
counter = count(3, 3)
n_abc = cycle(abc_list)
new_abc = [next(n_abc) for el in range(n)]
new_list = [next(counter) for num in range(n)]
print(new_abc)
print(new_list)
set_abc = set(new_abc)
print(set_abc)

