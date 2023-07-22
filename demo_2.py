# class C:
#     def __init__(self, var):
#         self.a = var
#
#
# a = C(12)
#
# b = C(20)
#
# print(a.a, b.a)


class CC:

    def __init__(self, var):
        self._a = var

    def gget(self):
        print("Getting a")
        return self._a

    def gset(self, new_var):
        print("Setting a")
        self._a = new_var

    def gdel(self):
        print("DELETING a")

    a = property(gget, gset, gdel)

cc = CC(10)
print(cc.a)
cc.a = 200
print(cc.a)
del cc.a