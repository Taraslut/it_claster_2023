import re

line = "hello word! my name is Taras. that is easy."


def make_title(l: str) -> str:
    is_start_sentence = True
    rez = ""
    for letter in l:
        if letter in '.!?':
            is_start_sentence = True

        if is_start_sentence and letter.isalpha():
            rez += letter.upper()
            is_start_sentence = False
        else:
            rez += letter

    return rez


print(make_title(line))
assert make_title(line) == "Hello word! My name is Taras. That is easy."
