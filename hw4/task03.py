import sys


def my_precious_logger(text: str):
    if text.split()[0][:5].upper() == 'ERROR':
        print(text, file=sys.stderr)
    else:
        print(text)  # default value for 'file' argument in 'print' function is file=sys.stdout.
