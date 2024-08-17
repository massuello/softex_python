# #lambda
# def myfuctio(n):
#     return lambda a: a * n
#
# mydoubler = myfuctio(2)
# mytripler = myfuctio(3)
#
#
# print(mydoubler(11))
# print(mytripler(11))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
