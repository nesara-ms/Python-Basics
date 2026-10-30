# 5.Dictionary Comprehension
#Creating a dictionary of squares
numbers = [1,2,3,4,5]
dict_square = {num:num**2 for num in numbers}
print(dict_square)

#Converting a list of names to a dictionary of name lengths
names = ["Neha","Kushal","Nesara"]
name_length = {name:len(name) for name in names}
print(name_length)

#Filtering cities with population above 10 lakhs
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)