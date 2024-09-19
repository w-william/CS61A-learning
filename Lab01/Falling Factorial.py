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
    result = 1
    if k == 0:
        return result
    else:
        while k != 0 and n != 0 :
            result *= n
            n -= 1
            k -= 1
        return result

print(falling(4, 5))