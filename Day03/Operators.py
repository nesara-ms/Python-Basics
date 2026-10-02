'Operators in python.'
# 1. Arithmetic Operators : +, -, *, /, %, **, //
a = 10
b = 3
print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)  # Division
print("Modulus:", a % b)  # Modulus
print("Exponentiation:", a ** b)  # Exponentiation
print("Floor Division:", a // b)  # Floor Division

#2. Comparison Operators : ==, !=, >, <, >=, <=
x = 5
y = 10
print("Equal:", x == y)  # Equal
print("Not Equal:", x != y)  # Not Equal
print("Greater Than:", x > y)  # Greater Than
print("Less Than:", x < y)  # Less Than
print("Greater Than or Equal:", x >= y)  # Greater Than or Equal
print("Less Than or Equal:", x <= y)  # Less Than or Equal

#3. Logical Operators : and, or, not
#not>and>or (precedence)
p = True
q = False
print("and:", p and q)  # and
print("or:", p or q)  # or
print("not:", not p)  # not

#4. Assignment Operators : =, +=, -=, *=, /=, %=, **=, //=
c = 5
print("c =", c)
c += 3  # Equivalent to c = c + 3
print("c += 3:", c)
c -= 2  # Equivalent to c = c - 2
print("c -= 2:", c)
c *= 4  # Equivalent to c = c * 4
print("c *= 4:", c)
c /= 2  # Equivalent to c = c / 2
print("c /= 2:", c)
c %= 3  # Equivalent to c = c % 3
print("c %= 3:", c)
c **= 2  # Equivalent to c = c ** 2
print("c **= 2:", c)
c //= 2  # Equivalent to c = c // 2
print("c //= 2:", c)

#5. Bitwise Operators : &, |, ^, ~, <<, >>
m = 5  # Binary: 0101
n = 3  # Binary: 0011
print("m & n:", m & n)  # Bitwise AND
print("m | n:", m | n)  # Bitwise OR
print("m ^ n:", m ^ n)  # Bitwise XOR
print("~m:", ~m)  # Bitwise NOT
print("m << 1:", m << 1)  # Left Shift
print("m >> 1:", m >> 1)  # Right Shift

#6. Membership Operators : in, not in
list1 = [1, 2, 3, 4, 5]
print("3 in list1:", 3 in list1)  # in
print("6 not in list1:", 6 not in list1)  # not in

#7. Identity Operators : is, is not
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a is b:", a is b)  # is
print("a is c:", a is c)  # is
print("a is not b:", a is not b)  # is not