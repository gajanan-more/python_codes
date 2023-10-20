"""
Variable Rules:
- Variable must start with letter or underscore.
- Variable can not start with number.
- Variable name should contain alpha-umber char and underscores (A-Z, a-z, 0-9, _).
- Variables are case sensitive: 'x' and 'X' are different variables.
- Reserved keywords can not be used as variable name. If you want to check whether the variable name is
reserved keyword, you can use `iskeyword()`, if it is keyword, it will return `True`. For that, we have to
import `keyword` library.

Example of Valid Variable Names: abc, a1, a_1, asd56_asd, _asd
Example of Invalid Variable Names: ab*c, a$1, a-1, 9sdf

"""
import keyword

"""
We don't need to mention the data type while declaring the variable in python.

How to declare a variable and assign the value:

variable_name = (assignment_operator) value
"""
username = "admin"

# To print the value in the variable
print(username)

# To check if `username` is part of reserved keyword or not: iskeyword()
print("Check of reserved keyword:",keyword.iskeyword("username"))

print("Check of reserved keyword:",keyword.iskeyword("and"))


# To get the reserved keyword list:
print("\n ======================== \n",keyword.kwlist,"\n ======================== \n")

# To check the type of the varible: type()
print("Type of variable 'username':", type(username))

"""
Example:
data types in python:
<class 'int'>
<class 'float'>
<class 'string'>
<class 'list'>
<class 'dict'>
"""

# Variables with different data types
x = 12
print("Type of variable 'x':",type(x))

y = 1.34
print("Type of variable 'y':",type(y))

z = [1,2.3,4]
print("Type of variable 'z':",type(z))

w = {'a': 1, 'b': 2}
print("Type of variable 'w':",type(w))

u = {2,3,4,5}
print("Type of variable 'u':",type(u))

v = (1,2,4)
print("Type of variable 'v':",type(v))

# To update the value in the variable
username = "admin2"

print(username)

# To assign the value of one variable to another variable

password = username

print(password)

# To get the address of the variable: id()
print("Memory Address of variable 'username'",id(username))
print("Memory Address of variable 'password'",id(password))

"""
Here, we have assigned the value of variable 'username' to variable 'password'
That's why we are getting same memory address. 
"""

password = "password"

print(password)

print("Memory Address of updated variable 'password'",id(password))

# To get the ASCII value of the alphabet, number, special character: ord()

print("ASCII Value of 'a':",ord('a'))
print("ASCII Value of 'z':",ord('z'))
print("ASCII Value of 'A':",ord('A'))
print("ASCII Value of 'Z':",ord('Z'))
print("ASCII Value of '1':",ord('1'))
print("ASCII Value of '9':",ord('9'))
print("ASCII Value of '0':",ord('0'))
print("ASCII Value of '*':",ord('*'))

# To get the alphabet, number, special character on the ASCII value: chr()
# Valid ASCII Values: 0 to 127

print("Character at ASCII value 97:",chr(97))
print("Character at ASCII value 122:",chr(122))
print("Character at ASCII value 65:",chr(65))
print("Character at ASCII value 90:",chr(90))
print("Character at ASCII value 49:",chr(49))
print("Character at ASCII value 57:",chr(57))
print("Character at ASCII value 48:",chr(48))
print("Character at ASCII value 42:",chr(42))





