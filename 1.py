# 1. TODO Напишіть програму, яка виводить всі числа від x до y


def print_num():
    first_num = int(input("Введіть перше число:"))
    last_num = int(input("Введіть останє число:"))
    if first_num >= last_num:
        return print("Перше число має бути менше другого!!!")
    else:

        for num in range(first_num, last_num + 1):
            print(num)


print_num()
