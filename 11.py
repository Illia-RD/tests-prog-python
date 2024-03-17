# 11. TODO Напишіть програму, яка обчислює суму квадратів чисел від 1 до N


def input_data():
    last_num_input = int(input("введіть кінцеве число діапазону \n"))
    return last_num_input


# цикл for


def range_squere(last_num):
    squered_numbers = []
    for num in range(1, last_num + 1):
        squered_numbers.append(num**2)
    print(squered_numbers)


# list comprehension
"""
def range_squere(last_num):
    squered_numbers = [num**2 for num in range(1, last_num + 1)]
    print(squered_numbers)

"""


# функція map
"""
def range_squere(last_num):
    squered_numbers = list(map(lambda x: x**2, range(1, last_num + 1)))
    print(squered_numbers)

"""


# функція pow
"""
def range_squere(last_num):
    squered_numbers = [pow(num, 2) for num in range(1, last_num + 1)]
    print(squered_numbers)

"""


range_squere(input_data())
