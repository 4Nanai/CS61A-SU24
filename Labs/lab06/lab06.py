def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    
    i, j = 0 ,0
    while i < n:
        a = next(t)
        if a == x:
            j += 1
        i += 1
    return j


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"

    if n >= 1:
        yield n
        if n % 2 == 0:
            yield from hailstone(n // 2)
        elif n % 2 == 1 and n != 1:
            yield from hailstone(n * 3 + 1)
    


def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may or may not
    be infinite sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, None), next(iter_b, None)
    # print("DEBUG: next_a, next_b =", next_a, next_b)
    "*** YOUR CODE HERE ***"

    # if not all(x is None for x in incr_a) and not all(x is None for x in incr_b):
    #     if next_a == next_b:
    #         print("DEBUG: a = b, a =", next_a)
    #         yield next_a
    #         yield from merge([next(iter_a, None) for _ in range(10)], [next(iter_b, None) for _ in range(10)])
    #     elif next_a < next_b:
    #         print("DEBUG: a < b, a =", next_a)
    #         yield next_a
    #         yield from merge([next(iter_a, None) for _ in range(10)], [next_b] + [next(iter_b, None) for _ in range(10)])
    #     else:
    #         print("DEBUG: a > b, b =", next_b)
    #         yield next_b
    #         yield from merge([next_a] + [next(iter_a, None) for _ in range(10)], [next(iter_b, None) for _ in range(10)])

    # elif all(x is None for x in incr_b) and not all(x is None for x in incr_a):
    #     print("DEBUG: empty incr_b, a =", next_a)
    #     yield next_a
    #     yield from merge([next(iter_a, None) for _ in range(10)], [])
    # elif all(x is None for x in incr_a) and not all(x is None for x in incr_b):
    #     print("DEBUG: empty incr_b, b =", next_b)
    #     yield next_b
    #     yield from merge([], [next(iter_b, None) for _ in range(10)])

    while next_a is not None and next_b is not None:
        if next_a == next_b:
            yield next_a
            next_a = next(iter_a, None)
            next_b = next(iter_b, None)
            # print("DEBUG: a = b, next_a, next_b =", next_a, next_b)
        elif next_a < next_b:
            yield next_a
            next_a = next(iter_a, None)
            # print("DEBUG: a < b, next_a, next_b =", next_a, next_b)
        elif next_a > next_b:
            yield next_b
            next_b = next(iter_b, None)
            # print("DEBUG: a > b, next_a, next_b =", next_a, next_b)
    
    while next_a is None and next_b is not None:
        yield next_b
        next_b = next(iter_b, None)
    while next_a is not None and next_b is None:
        yield next_a
        next_a = next(iter_a, None)
    


def deep_map(f, s):
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"

    if type(s) != list:
        s = [s]
    iter_s = iter(s)
    next_s = next(iter_s, None)
    i = 0
    print("DEBUG:",s)
    while next_s is not None:
        print("DEBUG:",i)
        if type(next_s) != list:
            s[i] = f(s[i])
            next_s = next(iter_s, None)
            i += 1
        else:
            deep_map(f, s[i])
            next_s = next(iter_s, None)
            i += 1
    '''
    for i in range(len(s)):
        if type(s[i]) is list:
            deep_map(f, s[i])
        else:
            s[i] = f(s[i])
    '''
    return None


def buy(required_fruits, prices, total_amount):
    """Print ways to buy some of each fruit so that the sum of prices is amount.

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)
    [2 apples][1 orange][1 banana]
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    [2 apples][1 orange][3 bananas]
    [2 apples][2 oranges][1 banana]
    >>> buy(['apples', 'kiwis'], prices, 36)
    [3 apples][3 kiwis]
    [6 apples][2 kiwis]
    [9 apples][1 kiwi]
    """

    def add(fruits, amount, cart):
        if fruits == [] and amount == 0:
            print(cart)
        elif fruits and amount > 0:
            fruit = fruits[0]
            price = prices[fruit]
            for k in range(1, amount // price + 1):
                add(fruits[1:], amount - price * k, cart + display(fruit, k))
    add(required_fruits, total_amount, '')


def display(fruit, count):
    """Display a count of a fruit in square brackets.

    >>> display('apples', 3)
    '[3 apples]'
    >>> display('apples', 1)
    '[1 apple]'
    """
    assert count >= 1 and fruit[-1] == 's'
    if count == 1:
        fruit = fruit[:-1]  # get rid of the plural s
    return '[' + str(count) + ' ' + fruit + ']'



