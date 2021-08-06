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

	# code up your solution here
	return a+b, abs(a-b)


def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
	return lambda base, height: base * height / 2 


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

	# code up your solution here
	return '-'.join(sorted( hyphen_str.split('-')))


def perfect_number( number):
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
	# code up your answer here
	# for an arbitrary number, find the positive divisors bound;
	# note that int(float) == floor(float),
	# it is good to have a looser bound, so max_bound = int(float)+1.
	# it may waste some computational power, but it is safer.
	min_prop_divd = 1 
	max_prop_divd = int(number / 2) + 1   

	# loop to look for the maximum proper divisors
	sum_fac = 0
	for i in range( min_prop_divd, max_prop_divd + 1):
		if number % i == 0:
			sum_fac += i 

	# check if the number is a perfect number
	return sum_fac == number 

## To test the solution of Q4, we use a function
def check_Q4():
	'''
	Loop to find the perfect word within 0-10,000.
	'''
	perfect_nums = []
	for num in range(2, int(1e4)):
		if perfect_number( num):
			perfect_nums.append( num)
	return perfect_nums

if __name__ == '__main__':
	
	# Test my answer 
	print( f' The sum for 40 and 10 is: {calculation( 40, 10)[0]},\n and the substraction is {calculation( 40, 10)[1]}')
	print( f' The area of a triangle with base=3 and height=4 is: {triangle_lambda()( 3, 4)}')
	print( f' The sorted string of \'green-red-yellow-black-white\': {sort_words("green-red-yellow-black-white")}')
	print( f' The perfect number within 2-10,000 are: {check_Q4()}')
	