#While loops in python are used to execute a block of code repeatedly as long as a given condition is true. The syntax for a while loop is as follows:
i = 1
while i <= 5:
  print(i)
  if (i == 3):
    break
  i += 1
print("end of loop")

#using "while" loop, pratice questions
n = 5
sum = 0
i = 1
while i<=n:
     sum += i
     i+=1
print("Total sum=",sum)

n = 5
fact = 1
count = 1
while count<=n:
    fact*= count
    count+= 1
print("Factorial=",fact)



