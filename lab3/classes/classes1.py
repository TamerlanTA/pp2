class StringManipulator:
    def airpods(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())


sm = StringManipulator()
sm.getString() 
sm.printString() 