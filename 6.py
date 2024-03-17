# 6. TODO Напишіть програму, яка проводить арифметичні операції над двома числами, введеними користувачем


def input_data():
    input_first_num = int(input("введіть перше число: "))
    input_second_num = int(input("введіть друге число: "))
    input_option = input("Оберіть дію(+, -, *, /): ")
    return input_first_num, input_second_num, input_option


def calc(data):
    first_num, second_num, option = data
    if option == "+":
        res = first_num + second_num
    elif option == "-":
        res = first_num - second_num
    elif option == "*":
        res = first_num * second_num
    elif option == "/":
        res = first_num / second_num
    else:
        res = f"Помилка! Дію {option} не знайдено. Виберіть дію з списку перечислених"
    return res


print(calc(input_data()))
