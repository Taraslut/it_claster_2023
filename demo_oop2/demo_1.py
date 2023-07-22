class A:
    def __init__(self):
        print("In A init")
        self.a = 18

    def show_info(self):
        print("I'm in calass A ")
        return "I'm in calass A "

a = A()

a.show_info()
print(a.a)

print("="*20)


class D(A):
    def __init__(self):
        print("In D init")
        super().__init__()
        self.d = 100

print("="*20)

class B(A):
    def __init__(self):
        print("In B init")
        super().__init__()
        self.b = 67

    def show_info(self):
        print("I'm in class B")
        return "I'm in class B "

b = B()
print(b.b)

b.show_info()
print(b.a)
print(B.__mro__)
print(A.__subclasses__())
