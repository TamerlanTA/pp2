class shape:
    def __init__ (self):
        self.length = int(input())
        self.width = int(input())
    def area(self):
        return 0
    
class rectangle(shape):
    def __init__(self):
        self.length = int(input())
        self.width = int(input())
    def area(self):
        return self.length * self.width

myRectangle = rectangle()
print(myRectangle.area())