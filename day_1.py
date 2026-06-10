Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "gaurav patil"
s
'gaurav patil'
s.capitalize()
'Gaurav patil'
s.upper()
'GAURAV PATIL'
s
'gaurav patil'
# string is Immutable data type in python
# we can not change original objecst
s
'gaurav patil'
# In Python data types we have 2 options
# 1. Mutable
# 2. Immutable
#--------------------------------------------
# comment
#-------------------------------------------
# Identifier- a name give to the object
# Object - is a physical entity present in the program/memory
100
100
"python"
'python'
4.55
4.55
x = 100
# x is an identifier
# 100 is an object
y = "python"
y
'python'
z = 4.55
z
4.55
# we have 3 objects and 3 idetifies
# identifiers are also known as variables
#--------------------------
# RUles of declaring an ideitifier
# a-zA-Z allowed
# _ is allowed
first name = 'python'
SyntaxError: invalid syntax
# space is not allowed
first_name = 'python'
first_name
'python'
# Special symbols and chars are not allowed
first&name = 'python'
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
first$name = 'python'
SyntaxError: invalid syntax
#-------------------
# Number as a prefix not allowed
1num = 100
SyntaxError: invalid decimal literal
2_pin = 1234
SyntaxError: invalid decimal literal
# Number as a suffix is allowed
num1 = 100
num1
100
#----------------------
# dont use reserve keywords
in = 99
SyntaxError: invalid syntax
# to check freserve keyword we have keyword library
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
del = 100
SyntaxError: invalid syntax
len(keyword.kwlist)
35
