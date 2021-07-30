from functools import reduce

good_numbers = [n for n in range(100, 1001) if n % 2 == 0]
print(good_numbers)
multiply_numbers = reduce(lambda a, b: a * b, good_numbers, 1)
print(multiply_numbers)
