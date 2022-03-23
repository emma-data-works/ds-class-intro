'''
Edit this file to complete Exercise 6
'''

def calculation(a, b):
	'''
	Write a function calculation() such that it can accept two variables 
	and calculate the addition and subtraction of it. 
	It must return both addition and subtraction in a single return call

	Expected output:
	res = calculation(40, 10)
	print(res)
	>>> (50, 30)

	Arguments:
	a: first number 
	b: second number

	Returns:
	sum: sum of two numbers
	diff: difference of two numbers
	'''
	if (a != None and b !=None):
		sum_result = a+b
		sub_result = a-b
	return sum_result,sub_result


def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
	return lambda base,height : base*height/2


def sort_words(hyphen_str):
	'''
	Write a Python program that accepts a hyphen-separated sequence of words 
	as input, and prints the words in a hyphen-separated sequence after 
	sorting them alphabetically.

	Expected output:
	sort_words('green-red-yellow-black-white')
	>>> 'black-green-red-white-yellow'
	
	Arguments:
	hyphen_str: input string separated by hyphen

	Returns:
	sorted_str: string in a hyphen-separated sequence after 
	sorting them alphabetically
	'''

	# note input: dfdfw-cafdasere-bdsfaa-adfsare
	#1. string split to collection
	temp_arr=hyphen_str.split('-')
	#2. sort the collection
	temp_arr.sort()
	#3.join collection item with - seperator
	return '-'.join(temp_arr)





def perfect_number(num):
	'''
	Write a Python function to check whether a number is perfect or not.

	A perfect number is a positive integer that is equal to the sum of 
	its proper positive divisors. Equivalently, a perfect number is a number 
	that is half the sum of all of its positive divisors (including itself).

	Example: 6 is a perfect number as 1+2+3=6. Also by the second definition,
	(1+2+3+6)/2=6. Next perfect number is 28=1+2+4+7+14. Next two perfect
	numbers are 496 and 8128.

	Argument:
	number: number to check

	Returns:
	perfect: boolean, True if number is perfect
	'''
	factor_tuple = []
	for i in range(1,num+1):
		if(num%i==0 and i!=num):
			factor_tuple.append(i)
	if(sum(factor_tuple) == num):
		return True
	else:
		return False

if __name__ == '__main__':
	pass