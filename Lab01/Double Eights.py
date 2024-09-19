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
    num = 0
    while n != 0:
        if n % 10 == 8:
            num = n // 10
            if num % 10 == 8:
                print(True)
                break
        n = n // 10
    if n == 0:
        print(False)
double_eights(880808080)