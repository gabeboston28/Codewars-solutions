def descending_order(num):
    num2 = [int(i) for i in list(str(num))]
    num2.sort(reverse=True)
    return int(''.join([str(i) for i in num2]))
