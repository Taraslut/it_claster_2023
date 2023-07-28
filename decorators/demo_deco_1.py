def deco_info(f):
    def inner(*args, **kwargs):
        print("Call ", f.__name__, f"({args, kwargs})")
        rez_inner = f(*args, **kwargs)
        return rez_inner

    return inner


@deco_info  # line 13  is the same
def add(a: int, b: int) -> int:
    rez_add = a + b
    return rez_add


@deco_info
def sub(a, b):
    return a - b


# add = deco_info(add)
print(add(2, 4))
print(sub(9, 4))
