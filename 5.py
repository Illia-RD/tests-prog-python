# 5. TODO  Напишіть програму, яка обчислює факторіал числа, введеного користувачем.(1-N)


def calc_factorial(num_to_factorial):

    res = 1
    for num in range(1, num_to_factorial + 1):
        res *= num

    return res


# за допомогою бібліотеки math
"""
import math

def calc_factorial(num_to_factorial):
    res = math.factorial(num_to_factorial)
    return res
"""

input_num = int(input("введіть число: "))
print(calc_factorial(input_num))
