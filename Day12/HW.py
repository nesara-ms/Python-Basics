def calc_len(list):
    list = [10,20,30,40,50]
    print(len(list))
    return len
calc_len(list)

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
       fact*=i
    print(fact)
calc_fact(5)

    
def integer():
    num = int(input("Enter number:"))
    rem = num%2
    if (rem==0):
        print("EVEN")
    else:
        print("ODD")
integer()