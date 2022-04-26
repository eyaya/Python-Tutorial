
# I added this comment to test git add, commit and push today: April 26, 2022
def add(a,b):
	"""
	This fucntion adds two numbers and return the result
	"""
	c = a+b
	return c
	
def subtract(a,b):
	"""
	This fucntion substracts two numbers and return the result
	"""
	c = a-b
	return c
	
def multiply(a,b):
	"""
	This fucntion multiplies two numbers and return the result
	"""
	c = a*b
	return c
	
def divide(a,b):
	"""
	This fucntion divides two numbers and return the result
	"""
	if b==0:
		return("division by zero is not allowed")
	else:
		c = a/b
		return c
	
def absolute(a):
	"""
	A fucntion that computes the absolute value of a number
	"""
	if a <0:
		a *=-1
	return a
