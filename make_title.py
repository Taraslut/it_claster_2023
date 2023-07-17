line = "hello word! my name is Taras. that is easy."


def make_title(l: str) -> str:
    return l


print(make_title(line))
assert make_title(line) == "Hello word! My name is Taras. That is easy."
