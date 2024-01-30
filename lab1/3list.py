#example 1

thislist = ["apple", "banana", "cherry"]
print(thislist)

#example 2

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#example 3

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#example 4

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


#example 5

list1 = ["abc", 34, True, 40, "male"]

print(list1)

#example 6

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#example 7

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#example 8

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#example 9 

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#example 10

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#example 11

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#example 12

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#example 13

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#example 14

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#example 15
  
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example 16
  
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#example 17

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#example
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("-------")

#example
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print("-------")

#example
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("-------")

#example
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#example 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

#example
newlist = [x for x in range(10) if x < 5]

print(newlist)

#example 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#example 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#exmple 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

