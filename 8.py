# 8. TODO Напишіть програму, яка знаходить суму та середнє арифметичне чисел у списку


# варіант введення списку через цикл for
"""
def input_data():

    # Створення пустого списку
    numbers = []

    # Введення чисел з клавіатури
    for i in range(int(input("Введіть кількість чисел: "))):
        number = int(input("Введіть число: "))
        numbers.append(number)

    # Виведення списку
    print(f"Список: {numbers}")
"""


# список через input
def input_data():

    input_list = list(map(int, input("введіть список чисел через пропуск").split()))
    return input_list


# варіант без бібліотек через цикл for
def calc_list(data):

    total = 0
    for num in data:
        total += num
        print(
            f"Ви ввели список: {data}\n сума чисел списку: {total}\n середня значення чисел в списку, {total / len(data)}"
        )


# варіант через модуль statistics
"""
from statistics import mean
def calc_list(data):
    total_sum = sum(data)
        total_avr = mean(data)
        print(
         f"Ви ввели список: {data}\n сума чисел списку: {total_sum}\n середня значення чисел в списку, {total_avr}"
        )
"""


calc_list(input_data())
