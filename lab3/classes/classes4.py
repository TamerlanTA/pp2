import math

class point:
    def __init__ (self):
        self.x = int(input("x for point #1: "))
        self.y = int(input("y for point #1: "))
        self.x2 = int(input("x for point #2: "))
        self.y2 = int(input("y for point #2: "))
    def show(self):
        print("point #1 at: ", self.x, self.y)
        print("point #2 at: ", self.x2, self.y2)
    def move(self):
        self.x += int(input("move x #1: "))
        self.y += int(input("move y #1: "))
        self.x2 += int(input("move x #2: "))
        self.y2 += int(input("move y #2: "))
        print("point #1 at: ", self.x, self.y)
        print("point #2 at: ", self.x2, self.y2)
    def dist(self):
        return math.sqrt((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2)

we = point()
print(we.show())
print(we.move())
print(we.dist())


