def cubo(x):
    """
    La funciÃ³n cubo devuelve   x * x * x
    >>> cubo(3)
    27
    >>> cubo(-1)
    -1
    """
    return x*x*x

if __name__ == '__main__':
    import doctest
    doctest.ELLIPSIS
    doctest.testmod(verbose = True, optionflags=doctest.ELLIPSIS)