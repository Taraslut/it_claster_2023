def show_info(*args, **kwargs):
    for i in args:
        print(i)

    for k, v in kwargs.items():
        print(f"{k} = {v}")
