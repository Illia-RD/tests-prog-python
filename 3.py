# 3. TODO Напишіть програму, яка перевіряє, чи є введене число парним чи непарним


def checkNum(num):
    res = f"число {num} парне" if (num % 2) == 0 else f"число {num} непарне"
    return res


num = int(input("введіть число: "))
print(checkNum(num))
