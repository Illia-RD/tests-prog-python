# 13. TODO Напишіть програму, яка обчислює площу та периметр кола

import math


radius = float(input("введіть рдіус кола "))


def calc_area(r):
    s = math.pi * r**2
    print("Площа кола: ", s)


def calc_circumference(r):
    c = 2 * math.pi * r
    print("Радіус кола: ", c)


calc_area(radius)
calc_circumference(radius)
