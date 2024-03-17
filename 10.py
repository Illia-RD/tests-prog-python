# 10. TODO Напишіть програму, яка знаходить всі дільники заданого числа.


def input_data():
    num_input = int(input("введіть число \n"))
    return num_input


# _______________________цикл for_______________________


def find_devisors(number):
    devisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            devisors.append(i)
    return devisors


# _______________________comprehension (скорочений запис for)_______________________
"""
def find_devisors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

"""


# _______________________цикл while_______________________
"""
def find_devisors(number):
    devisors = []
    i = 1
    while i <= number:
        if numbner % i == 0:
            devisors.append(i)
        i += 1
    return devisors
"""

"""
модуль math

from math import sqrt


def find_devisors(number):
    devisors = [1]
    # print(f"number {number}, sqrt {sqrt(number)}")
    for i in range(2, int(sqrt(number)) + 1):
        # print(f"number{number} % i {i} = {number%i}")
        if number % i == 0:
            devisors.append(i)
            devisors.append(number // i)
            # print(f"i {i}, number // i -{number //i} = {number // i}")
    devisors.sort()
    return devisors

"""

print(find_devisors(input_data()))
