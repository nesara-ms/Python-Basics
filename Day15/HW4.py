# List of Square Numbers

l= [num**2 for num in range(1, 21)]

print(l)

# Student data task

st = [
      {
        'name': 'Neha', 
        'age': 19, 
        'grade': 85
        },

        {
         'name': 'Kushal',
        'age': 22,
        'grade': 90
        },
    ]

for student in st:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


# Dictionary comprehension

d = {
    "delhi": 90000,
    "mumbai": 120000,
    "bangalore": 80000,
}
print({key : value for key, value in d.items() if value > 100000 })

# Nested list challenge

row = int(input("Enter number of rows: "))

matrix = []

for i in range(row):
    r = [int(num) for num in input(f"Enter numbers for row {i+1} separated by space: ").split()]
    matrix.append(r)

print("The matrix is:",matrix)