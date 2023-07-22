class K:

    def __call__(self, *args, **kwargs):
        print(f"args {args}")
        print(f"kwargs {kwargs}")


f = K()
s = K()


s(2, "Hello", a= 4)
