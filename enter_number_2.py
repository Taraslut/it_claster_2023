while True:
    val = input("Enter your age: ")
    if any(l.isalpha() for l in val):
        print("You have to enter only digits")
        continue

    numb = int(val)
    break
print(f"Your age is {numb}")