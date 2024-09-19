def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """       
    count = 1
    n = int(n)
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
        print(n)
        count += 1
    return count
a = hailstone(4.0)
print(a)