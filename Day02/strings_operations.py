#String is a datatype, that stores a sequence of characters. escape sequences characters are the special characters which gives formatting.

'Basic escape sequences are: \n, \t, \\, \', \", \r, \b, \f, \v, \ooo, \xhh'

'Basic string operations are:'
#1. Concatenation: Joining two or more strings together using the + operator.
"hello" + " " + "world"  # Output: "hello world"

#2. length() function: Returns the number of characters in a string.
len("hello")  # Output: 5
str1 = "Neha"
len(str1)  # Output: 4
str2 = "Gowda"
len(str2)  # Output: 5

#3. Indexing: Accessing individual characters in a string using their index (position).
str = "Neha Gowda"
ch = str[0]  # Output: 'N'
ch = str[5]  # Output: 'G'
print(ch)  # Output: 'N' 'G'

#4. Slicing: Extracting a portion of a string using the slice operator.
str = "Neha Gowda"
sub_str = str[0:4]  # Output: "Neha"
print(sub_str)  # Output: "Neha"
print(str[5:len(str)])  # Output: "Gowda"

#5. Negative Indexing: Accessing characters from the end of the string using negative indices.
str = "Neha Gowda"
ch = str[-1]  # Output: 'a'
ch = str[-5]  # Output: 'G'
print(ch)  # Output: 'a' 'G'