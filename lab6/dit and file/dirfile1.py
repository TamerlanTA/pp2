import os
cd = os.chdir(input("Directory: "))
contents = os.listdir(cd)

n = 1
print("In current directory:")
for i in contents:
    print(f"{n}:", i)
    if os.path.isdir(i):
        print(f"    In {i}:")
        contents2 = os.listdir(i)
        print(contents2)
    n += 1

current_directory = os.getcwd()