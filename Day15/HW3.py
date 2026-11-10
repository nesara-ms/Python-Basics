# Ticket Booking System
seats = 8

while seats : # automatically checks if seats is not zero
    print(f"Available seats: {seats}")

    print("Book one seat")
    seats = seats - 1
    print(f"Seats left: {seats}")
print("All seats are booked!")

# countdown timer using time module
import time

countdown = 10
print("Countdown starts now!")
while countdown > 0:
    print(countdown)
    time.sleep(1)  # Wait for 1 second
    countdown -= 1


# Multiplication Table for 3 to 5

for i in range(3,6): #  # Loop through numbers 3 to 5
    for j in range(1, 11):  # Loop through numbers 1 to 10
        print(f"{i} x {j} = {i * j}")


# sum of first 10 natural numbers

total = 0
for i in range(1, 11):  # Loop through numbers 1 to 10
    
    total += i  # Add each number to total
    print(total)  # Print the current total after each addition

print("Sum of first 10 natural numbers:", total)


# printing a name letter by letter

name = 'Nehaa'

for letter in name:
    print(letter)


# counting vowels in a string

vowels = "aeiouAEIOU"

count = 0

text = "Hello, how are you doing today?"
for letter in text:
    if letter in vowels:
        count += 1

print("Number of vowels are :",count)


# Sum of prices in a dictionary

dishes = {
    "soup": 299,
    "burger": 899,
    "pizza": 799,
    "soda": 199
}

total_price = 0
for key, value in dishes.items():
    total_price += value  # Add each dish's price to total_price

print("Total prices :",total_price)

# OR

print(sum(dishes.values()))