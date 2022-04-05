from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    >>> fizzbuzz(0)
    []
    """
    result_list = []
    for i in range(1, n+1):
        if i % 15 == 0:
            result_list.append('fizzbuzz')
        elif i % 3 == 0:
            result_list.append('fizz')
        elif i % 5 == 0:
            result_list.append('buzz')
        else:
            result_list.append(f"{i}")
    return result_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
