# 14. TODO Напишіть програму, яка обчислює площу та периметр прямокутника за формулами


width_input = float(input("введіть  сторону A "))
height_input = float(input("введіть сторону B "))


def area(a, b):
    s = a * b
    print(s)


def perimetr(a, b):
    p = 2 * (a + b)
    print(p)


area(width_input, height_input)
perimetr(width_input, height_input)
