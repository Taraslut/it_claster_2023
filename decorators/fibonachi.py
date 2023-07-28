def deco_info(f):
    def inner(*args):
        print("Call ", f.__name__, f"{args}")
        rez_inner = f(*args)
        return rez_inner

    return inner


def deco_cash(f):
    f_rez = {}

    def inner(*args):
        if args not in f_rez:
            rez = f(*args)
            f_rez[args] = rez
        return f_rez[args]

    return inner


@deco_cash
@deco_info
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# 0 1 1 2 3 5 8 13 21
# assert fib(1) == 1
# assert fib(2) == 1
# # 5 = 3 + 2
# assert fib(5) == 5
#
# print(fib(8))
# print(fib(3))
for i in range(100):
    print("=" * 10)
    print(f"fib({i})=", fib(i))
