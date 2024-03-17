# 4. TODO Напишіть програму, яка виводить таблицю множення для числа, введеного користувачем.


def mult_num(n):
    for mult in range(1, 11):
        print(f"{n} * {mult} = {n*mult}")


num = int(input("введіть число: "))
print(mult_num(num))
