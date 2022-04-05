def fizzbuzz(n: int):
    """
    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']

    >>> list(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield 'fizzbuzz'
        elif i % 3 == 0:
            yield 'fizz'
        elif i % 5 == 0:
            yield 'buzz'
        else:
            yield f"{i}"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
