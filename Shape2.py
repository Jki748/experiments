def Shape(x, y):
    return getArea(x, y)


class getArea():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def Triangle(self):
        return (self.length * self.width) / 2

    def Rectangle(self):
        return self.length * self.width


print(Shape(5, 10).Triangle())
print(Shape(5, 10).Rectangle())