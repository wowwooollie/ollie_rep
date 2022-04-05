from ollie_rep.hw4.task02 import read_magic_number
import pytest


@pytest.mark.parametrize('file_string', ['1\nhello\nthat"s a test',
                                         '1.5\nlalaland',
                                         '2.999999\nMaMMA MIA!'])
def test_read_magic_number_positive(file_string):
    path = 'my_test_file.txt'
    with open(path, 'w') as f:
        f.write(file_string)
    assert read_magic_number(path) is True


@pytest.mark.parametrize('file_string', ['0\nhello\nMouline Rouge',
                                         '5\nSouth Park: Bigger, Longer & Uncut',
                                         '3\nRocket Man'])
def test_read_magic_number_negative(file_string):
    path = 'my_test_file.txt'
    with open(path, 'w') as f:
        f.write(file_string)
    assert read_magic_number(path) is False


def test_read_magic_number_error():
    path = 'my_test_file.txt'
    with open(path, 'w') as f:
        f.write('AND THE BEST ONE\nIS DEFINITELY "THE GREATEST SHOWMAN"')
    with pytest.raises(ValueError):
        read_magic_number(path)
