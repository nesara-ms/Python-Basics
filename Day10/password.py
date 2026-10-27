#password validations
password = 1234
input_password = int(input("Enter your password:"))
if password == input_password:
    print("Access granted")
else:
    print("Access denied")

# Password validation with retry limit
attempts = 0
password1 = 1234
while attempts < 3:
    in_password = int(input("Enter your password: "))

    if password1 == in_password :
        print("Access granted")
        break
    else:
        print("Wrong password, try again")
        print("You have", 2- attempts, "attempts left")
        attempts += 1
