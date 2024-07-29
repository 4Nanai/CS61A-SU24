def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"

    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        while k > 1:
            k = k - 1
            return n * falling(n-1,k)



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"

    Num_test, total = 1, 0
    while Num_test <= n:
        if Num_test % k == 0:
            total = total + 1
            print(Num_test)
            Num_test = Num_test + 1
        else:
            Num_test = Num_test + 1
    return total


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    num_wto_last, last = y // 10, y % 10
    if y < 10:
        return y
    else:
        return last + sum_digits(num_wto_last)
    

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    def split(n):
        num_wto_last, last = n // 10, n % 10
        return num_wto_last, last
    num_wto_last, last = split(n)
    while num_wto_last > 0:
        if last == 8:
            num_wto_last, last = split(num_wto_last)
            if last == 8:
                return True
            else:
                num_wto_last, last = split(num_wto_last)
        else:
            num_wto_last, last = split(num_wto_last)
    return False 
