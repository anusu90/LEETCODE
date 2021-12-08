string = 'vishal'


def shifting(string, n):
    out = ""
    for x in string:
        out = out+chr(ord(x)+n if ord(x)+n <= 122 else ord(x) + n - 26)
    return out


def unshifting(string, n):
    out = ""
    for x in string:
        out = out+chr(ord(x) - n if ord(x) - n >= 97 else ord(x) - n + 26)
    return out
