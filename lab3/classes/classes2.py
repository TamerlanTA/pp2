class shape:
    def area(self):
        return 0
    
class square(shape):
    def __init__(self, length):
        length = int(input())
        self.length = length
    def area(self):
        return self.length ** 2

mysquare = square(shape)
print(mysquare.area())