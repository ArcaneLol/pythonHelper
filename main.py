def getEven(num1 = 1, num2 = 1, num3 = 0):
    """
        num1 is the point where the even number starts and num2 where the search should end.
        To work, dont use num3 in same syntax.

        num3 is only able to work if num2 is not filled, num1 stands for the start of the search.
    """
    sum  = []
    if num3 != 0:
        for i in range(num1, num3*2+1):
            if i%2 == 0:
                sum.append(i)
    else:
        for i in range(num1, num2):
            if i%2 == 0:
                sum.append(i)
    return sum
