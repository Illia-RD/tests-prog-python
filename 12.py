# 12. TODO Напишіть програму, що додає два списки з числами та сортує їх в порядку зростання
def input_data():
    input_first_list = list(
        map(int, input("введіть перший список чисел через пропуск \n ").split())
    )
    input_second_list = list(
        map(int, input("введіть другий список чисел через пропуск \n ").split())
    )
    return (input_first_list, input_second_list)


# оператор +


def calc_lists(data):
    first_list, second_list = list(data)
    res = first_list + second_list
    res.sort()
    print(res)


# метод extend
"""
def calc_lists(data):
    first_list, second_list = list(data)
    first_list.extend(second_list)
    first_list.sort()
    print(first_list)

"""

calc_lists(input_data())
