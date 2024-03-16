# # TODO 1. Напишіть програму, яка виводить всі числа від x до y


# def print_num():
#     first_num = int(input("Введіть перше число:"))
#     last_num = int(input("Введіть останє число:"))
#     if first_num >= last_num:
#         return print("Перше число має бути менше другого!!!")
#     else:

#         for num in range(first_num, last_num + 1):
#             print(num)


# print_num()

# TODO Напишіть програму, яка обчислює суму перших 0 - N натуральних чисел.


# def sum_num():
#     l_num = int(input("введіть кінцеве натуральне число "))
#     f_num = 0
#     error = "кінцеве число не може бути менше чи дорівнювати початковому!!!"
#     if l_num <= f_num:
#         print(error)
#     else:
#         res = sum(range(0, l_num + 1))
#         print(f"сума всіх чисел від {f_num}, до {l_num} дорівнює {res}")


# sum_num()

# TODO Напишіть програму, яка перевіряє, чи є введене число парним чи непарним


# def checkNum(num):
#     res = f"число {num} парне" if (num % 2) == 0 else f"число {num} непарне"
#     return res


# num = int(input("введіть число: "))
# print(checkNum(num))

# TODO Напишіть програму, яка виводить таблицю множення для числа, введеного користувачем.


# def mult_num(n):
#     for mult in range(1, 11):
#         print(f"{n} * {mult} = {n*mult}")


# num = int(input("введіть число: "))
# print(mult_num(num))

# TODO  Напишіть програму, яка обчислює факторіал числа, введеного користувачем.(1-N)

# import math


# def calc_factorial(num_to_factorial):
#     res = math.factorial(num_to_factorial)
#     # res = 1
#     # for num in range(1, num_to_factorial + 1):
#     #     res *= num

#     return res


# input_num = int(input("введіть число: "))
# print(calc_factorial(input_num))

# TODO Напишіть програму, яка проводить арифметичні операції над двома числами, введеними користувачем


# def input_data():
#     input_first_num = int(input("введіть перше число: "))
#     input_second_num = int(input("введіть друге число: "))
#     input_option = input("Оберіть дію(+, -, *, /): ")
#     return input_first_num, input_second_num, input_option


# def calc(data):
#     first_num, second_num, option = data
#     if option == "+":
#         res = first_num + second_num
#     elif option == "-":
#         res = first_num - second_num
#     elif option == "*":
#         res = first_num * second_num
#     elif option == "/":
#         res = first_num / second_num
#     else:
#         res = f"Помилка! Дію {option} не знайдено. Виберіть дію з списку перечислених"
#     return res


# print(calc(input_data()))

# TODO Напишіть програму, яка піднімає введене користувачем число до степеня, введеного користувачем

# import math


# def input_data():
#     input_num = float(input("введіть  число: "))
#     input_power = float(input("до якого степеня підносимо число? "))
#     return input_num, input_power


# def power_of(data):
#     num, power = data
#     res = math.pow(num, power)  # через бібліотеку math
#     # res = num**power # на чистому пітоні
#     return res


# print(power_of(input_data()))


# Напишіть програму, яка знаходить суму та середнє арифметичне чисел у списку
# def input_data():
#     # варіант введення списку через цикл for
#     """
#     # Створення пустого списку
#     numbers = []

#     # Введення чисел з клавіатури
#     for i in range(int(input("Введіть кількість чисел: "))):
#         number = int(input("Введіть число: "))
#         numbers.append(number)

#     # Виведення списку
#     print(f"Список: {numbers}")
#     """
#     input_list = list(map(int, input("введіть список чисел через пропуск").split()))
#     return input_list


# from statistics import mean


# def calc_list(data):
#     # варіант без бібліотек через цикл for

#     total = 0
#     for num in data:
#         total += num
#         print(
#             f"Ви ввели список: {data}\n сума чисел списку: {total}\n середня значення чисел в списку, {total / len(data)}"
#         )

#     # варіант через модуль statistics


# """
#     total_sum = sum(data)
#         total_avr = mean(data)
#         print(
#          f"Ви ввели список: {data}\n сума чисел списку: {total_sum}\n середня значення чисел в списку, {total_avr}"
#         )
# """


# calc_list(input_data())

# TODO Напишіть програму, яка визначає, чи є введений рік високосним.


# def input_data():
#     year_input = int(input("введіть рік \n"))
#     return year_input

# # на чистому пітоні

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return f"{year} не високосний"

#         return f"{year} рік високосний"
#     else:
#         return f"{year} рік не високосний"


# # модуль datatime
# """
# from datetime import datetime


# def is_leap_year(year):
#     try:
#         datetime(year, 2, 29)
#         return f"{year} рік високосний"
#     except ValueError:
#         return f"{year} рік не високосний"

# """
# #вбудована функція calendar
# """
# import calendar

# def is_leap_year(year):

#     return (
#         f"{year} рік високосний"
#         if calendar.isleap(year) == True
#         else f"{year} рік не високосний"
#     )
# """
# print(is_leap_year(input_data()))

# TODO Напишіть програму, яка знаходить всі дільники заданого числа.


def input_data():
    num_input = int(input("введіть число \n"))
    return num_input


# цикл for
"""
def find_devisors(number):
    devisors = []
    for i in range(1, number + 1):
        if numbner % i == 0:
            devisors.append(i)
    return devisors
"""


# comprehension (скорочений запис for)


# def find_devisors(number):
#     return [i for i in range(1, number + 1) if number % i == 0]


# цикл while
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

# print(find_devisors(input_data()))
