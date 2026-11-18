# Functions

def greet():
    print("Hello, welcome to the program!")

greet()


# Function with parameters
def marriage(boy,girl):
    print(f"{boy} married {girl}")

marriage("Virat", "Anushka") #position of arguments
marriage(boy="Chandan", girl="Neha") #keyword arguments


# Function with default parameters
def marriage2(boy="alex",girl="sophia"):
    print(f"{boy} married {girl}")

marriage2() # calling the function without arguments
marriage2(girl="amrita") # calling the function with arguments


# Function with default parameters
def tables(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

tables(500) # calling the function with an argument
tables(10)


def func(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

func(10) # calling the function with an argument

def func2(num):
    print(int(str(num)*5))

func2(10) # calling the function with an argument


def func3():
    print(a) # function without parameters

a="Nehaa" #global variable
func3() # calling the function without an argument