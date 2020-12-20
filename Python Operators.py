Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=3
>>> print(x)
3
>>> 
>>> #define new variable with name x and value 2.0
>>> x=2.0
>>> print(x)
2.0
>>> #prove that this variable is float
>>> type(x)
<class 'float'>
>>> #convert this variable to int
>>> x=int(x)
>>> type(x)
<class 'int'>
>>> #increase the x value by 6 using assignment operator
>>> x=x+6
>>> print(x)
8
>>> #get the module of the new x by 3
>>> x%3
2
>>> ----------------------------------------------------
SyntaxError: invalid syntax
>>> 
>>> #write s simple ternary operator
>>> x,y=5,6
>>> print("x" id x>y else "y")
SyntaxError: invalid syntax
>>> print("x" if x>y else "y")
y
>>> # ternary--> TRUE if {statement} else FALSE
>>> in elif , python will check all the conditios no matter what ? NO
SyntaxError: invalid syntax
>>> #in elif we use else for ... ?
# it is reserved for the default
>>> 
>>> 
>>> '''
if we have this list [2,4,6,8,10] :
		- check to see if 4 in this list or not 
		- check to see if 4 and 6 in this list on not 
		- check to see if 3 or 6 in this list 
		- check to see if 2 , 4 and 5 in this list
'''
'\nif we have this list [2,4,6,8,10] :\n\t\t- check to see if 4 in this list or not \n\t\t- check to see if 4 and 6 in this list on not \n\t\t- check to see if 3 or 6 in this list \n\t\t- check to see if 2 , 4 and 5 in this list\n'
>>> y=[2,4,6,8,10]
>>> print(y)
[2, 4, 6, 8, 10]
>>> a=2
>>> if(a in list y):
	
SyntaxError: invalid syntax
>>> list=[2,4,6,8,10]
>>> print(list)
[2, 4, 6, 8, 10]
>>> a=2
>>> if a in list:
	print("found")
else("not found")
SyntaxError: invalid syntax
>>> print(a)
2
>>> print (list)
[2, 4, 6, 8, 10]
>>> if a in List
SyntaxError: invalid syntax
>>> if 2 in list:
	print("found")

	
found
>>> #check to see if 4 and 6 in this list on not
>>> if 6 and 4 in list:
	print("found")

	
found
>>> 
>>> 
>>> #check to see if 2 , 4 and 5 in this list
>>> if all(2,4,5) in list:
	print("found")
else print("Not found")
SyntaxError: invalid syntax
>>> if all(2,4,5) in list:
	print("found")
else print("Not found")
SyntaxError: invalid syntax
>>> if all (2,4,5) in list:
	print("found")
else:
	print("not found")

	
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    if all (2,4,5) in list:
TypeError: all() takes exactly one argument (3 given)
>>> 