import datetime

limit = 10_000_000

ll = []
start = datetime.datetime.now()
for i in range(limit):
    ll.append(i)
print(len(ll))
print(sum(ll))
print(f"time list processing for \t\t{(datetime.datetime.now() - start).microseconds} mcsec")

start = datetime.datetime.now()


def gen_items():
    for i in range(limit):
        yield i


ll = gen_items()

# print(len(ll))
print(sum(ll))
print(f"time generator processing for \t{(datetime.datetime.now() - start).microseconds} mcsec")
