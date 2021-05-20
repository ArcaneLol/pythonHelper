def getEven(num1 = 1, num2 = 1, num3 = 0):
    """
        num1 is the point where the even number starts and num2 where the search should end.
        To work, dont use num3 in same syntax.

        num3 is only able to work if num2 is not filled, num1 stands for the start of the search.
    """
    sum  = []
    if num3 != 0:
        for i in range(num1, num1+(num3*2)):
            if i%2 == 0:
                sum.append(i)
    else:
        for i in range(num1, num2+1):
            if i%2 == 0:
                sum.append(i)
    return sum

def getOdd(num1 = 1, num2 = 1, num3 = 0):
    """
        num1 is the point where the even number starts and num2 where the search should end.
        To work, dont use num3 in same syntax.

        num3 is only able to work if num2 is not filled, num1 stands for the start of the search.
    """
    sum  = []
    if num3 != 0:
        for i in range(num1, num1+(num3*2)):
            if i%2 != 0:
                sum.append(i)
    else:
        for i in range(num1, num2+1):
            if i%2 != 0:
                sum.append(i)
    return sum

def getPrimes(n):
    """ Gives you the prime numbers from 0 to n. """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]