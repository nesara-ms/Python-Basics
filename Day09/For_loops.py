#For loops

# FOR LOOP [01] prnt the elements
list = [1,4,9,16,36,49,64,81,100]
for el in list:
  print(el)

for el in range(5): #range(stop)
    print(el)

for el in range(1,5): #range(start, stop)
    print(el)

for el in range(1,5,2): #range(start,stop,step)
    print(el)

#can be used i instead or replace of el in programs,.
#range(start?,stop,step?) basically py understands 'starting' value tht means it should start wid 0 and 'step' is of 1 by default
# step increases value like step = 2 adre, it give 2 4 6 8 as output

# [01] prnt no,. from 1 to 100
for nums in range(1,101):
    print(nums)

#[02] 100 to 1
for nums in range(100,0,-1):
    print(nums)
    
#[03] prnt multi. table of a no.
n = int(input("enter number :"))
for i in range(1,11):
    print(n*i)

for i in range(5):
    pass
print("some useful work")

n = 5
sum = 0
for i in range(1, n+1):
     sum+= 1
print("Total sum=",sum)

#FACTORIAL of 1st n numbers[for]
n = 5
fact = 1
for n in range(1,n+1):
    fact*= n
print("Factorial:",fact)

name =  input("Enter your name: ")
for letter in name:
    print(letter)

for i in range(3,30,3):
    print(i)

sum = 0
for i in range(1, 11):
    sum += i
print("Total sum=", sum)

d = {"name": "Neha","age": 20, "income":0}
for key,value in d.items():
    print(key," ",value)

str = "hello,good morning"
vowels = "aeiou"
for char in str:
    for vowel in vowels:
        if char == vowel:
            print(char)