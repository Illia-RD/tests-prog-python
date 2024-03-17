# 7. TODO Напишіть програму, яка піднімає введене користувачем число до степеня, введеного користувачем


def input_data():
    input_num = float(input("введіть  число: "))
    input_power = float(input("до якого степеня підносимо число? "))
    return input_num, input_power


# на чистому пітоні
def power_of(data):
    num, power = data

    res = num**power
    return res


# через бібліотеку math
"""
import math

def power_of(data):
    num, power = data
    res = math.pow(num, power)  # через бібліотеку math
    return res

"""

print(power_of(input_data()))
