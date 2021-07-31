from functools import reduce

good_number = [n for n in range(100, 1001) if n % 2 == 0]
print(good_number)
multiply_numbers = reduce(lambda a, b: a * b, good_number, 1)
print(multiply_numbers)
