# print("hello world, its python time")
'This is a single quoted string'
"This is a double quoted string"
"""This is a triple qutoed string
and look at it what is can do"""
print("I said, \"Don't do it\"")
# here the \ is an escape character , when it saw double quote it will not end the string,but treat it as a 
# normal character
#in python also you have escape cahrcters like \n, for  new line, \t for tab, \r for carriage return
# \b for backspace, \f for form feed, \v for vertical tab, \a for bell, \0 for null character
# \uxxxx for unicode characters, where xxxx is the unicode value
# \Uxxxxxxxx for unicode characters, where xxxxxxxx is the unicode value
# \N{name} for unicode characters, where name is the name of the unicode character
# \o for octal value, \x for hexadecimal value
# print(type(12j*12j)) # complex numbers are represented as a + bj, where a is the real part and b is the imaginary part
# The output of the follwoing calculations will be a -144+0j, where -144 is the real part and 0 is the imaginary part
# Note the use of % operator , can be such that it is used preceeding to some aplhabetical charcters to indicaate , or to allocate 
# some space for the data type, like %d for integer, %f for float, %s for string, %c for character, %x for hexadecimal
# It behaves different,y when used like %%,example
print("The value of integer is given in %%d: %d" % 12)
print("The value of float is given in %%f: %f" % 12)
# In theis operations tehe %% is behaving like a normal % operator, but when used with a string it is used to format the string
# print("The value of string is given in %%s: %s" % "hello world")
# print((5/2))  # This will give the integer division of 5 by 2, which is 2.5
i =6
for i in range (6,15):
    print("the value of %d in octal is %%o:%o" %( i,i))
# Note that hwen you are printing a number with the use of formate specifier , you need to keep one thing in mind that is 
# you need to use the % operator before the variable name, and then use the variable name after the % operator
# This is because the % operator is used to format the string, and the variable name is  used to replace the value in the string
# print("The value of integer is given in %%d: %d" % 12)
j=9 
for j in range (9,20):
    print("The value of %d in hexadecimal is %%x: %x" %(j,j))
# Note that the % operator is used to format the string, and the variable name is used to replace the value in the string