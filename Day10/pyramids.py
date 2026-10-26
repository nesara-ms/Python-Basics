#pyramids using loops

"printing half pyramid using nested for loop"
n = int(input("enter number of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

"printing half pyramid using for loop"
n = int(input("enter number of rows:"))
for i in range(n):
    print("* " * (i+1))

"printing inverted half pyramid using nested for loop"
n = int(input("enter number of rows:"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()