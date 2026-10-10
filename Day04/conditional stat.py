''' conditional statements'''

#taking input from the user and printing it
'''name = input("name :")
age = int(input("age :"))
price = float(input("price :"))
print("my name is", name, "and i am ", age, "years of old")

#grades of students
marks = int(input("marks :"))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")

#pratice code
A = int(input("A :"))
G = input("M/F :")
if((A == 1 or A == 2)and G == "M"):
   print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 or G == "M"):
    print("fee is 300")
else:
    print("no fee")

#To find EVEN or ODD
num = int(input("enter number:"))
rem = num%2
if(rem==0):
   print("EVEN")
else:
   print("ODD")

#calculate the simple interest
p = float(input("p :"))
r = float(input("r :"))
t = float(input("t :"))

si = (p*r*t)/100
print(si)'

#input 2 numbers and print their sum
first = int(input("enter first:"))
second = int(input("enter second:"))
print("sum=", first + second)

#input side of square and print its area
side = float(input("enter the square side:"))
print("area=", side*side)

#input 2 floating point no. and print their avg
a = float(input("enter first:"))
b = float(input("enter second:"))
print("average=", (a+b)/2)

#input of 2 int no. a and b, print true a>=b if not false
a = int(input("enter first:"))
b = int(input("enter second:"))
print(a>=b)'''

#number from 1 to 10
for i in range(1,11):
  print(i,end="") 
  