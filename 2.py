# 2. TODO Напишіть програму, яка обчислює суму перших 0 - N натуральних чисел.


def sum_num():
    l_num = int(input("введіть кінцеве натуральне число "))
    f_num = 0
    error = "кінцеве число не може бути менше чи дорівнювати початковому!!!"
    if l_num <= f_num:
        print(error)
    else:
        res = sum(range(0, l_num + 1))
        print(f"сума всіх чисел від {f_num}, до {l_num} дорівнює {res}")


sum_num()
