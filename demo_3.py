class Human:

    def __init__(self):
        self.head = Head()
        self.arm = Arm()

class Head:
    def talk(self):
        return "Hello"

class Arm:

    def move(self):
        return "Move arm"

h = Human()

print(h.head.talk())
print(h.arm.move())