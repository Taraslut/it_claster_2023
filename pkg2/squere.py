from pkg1.helper import SOME_CONST

DEFAULT_SIZE = 10


def rise_square(val):
    if val > DEFAULT_SIZE:
        val = DEFAULT_SIZE
    print(f"{SOME_CONST} value {val}")

    rez = val * val
    return rez