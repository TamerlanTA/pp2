#Example

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Example

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)