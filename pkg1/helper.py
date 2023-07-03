from pkg_const import DEFAULT_SIZE

SOME_CONST = "Square"

def my_promt():
    print(f"{SOME_CONST} have to be less than {DEFAULT_SIZE}")
    rez = int(input(f"{SOME_CONST} size> "))
    return rez