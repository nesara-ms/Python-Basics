print("Arithmetic calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1-Addition (+) 2-Subtraction (-) 3-Multiplication (*) 4-Division (/)")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == 4:
   if num2 == 0:
        print("Error: Division by zero is not allowed.")
   else:
        print(f"{num1} / {num2} = {num1 / num2 :.2f}")
else:
        print("Invalid choice!")   