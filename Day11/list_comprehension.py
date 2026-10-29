# List Comprehension
#means-Creating list in a shorter way.
l = [2,4,6,8,10]
dl = [num*2 for num in l]
print(dl)

#squaring numbers in a list
numbers = [2,4,6,8,10]
square = [num ** 2 for num in numbers]
print(square)

#Filtering even numbers
numbers = [1,2,3,4,5,6,7,8]
even_numbers = [num % 2 == 0 for num in numbers]
print(even_numbers)

#Uppercasing Kannada city names
cities = ["Mandya","Mysuru","Bengaluru","Hubbali","Davengere"]
upper_case = [city.upper() for city in cities]
print(upper_case)


