#example 1

print(10 > 9)
print(10 == 9)
print(10 < 9)

#example 2 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example 3

print(bool("Hello"))
print(bool(15))

#example 4

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#example 5

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#example 6 

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#example 7 

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example 8

def myFunction() :
  return True

print(myFunction())

#example 9 

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#example 10 
  
x = 200
print(isinstance(x, int))
