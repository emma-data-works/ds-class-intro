'''
Edit this file to complete Exercise 5
'''
import numpy as np
# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


# code up your solution here
def number_finder(div, mul, start, end):
    """
    This is program is to print the number which in the start and end range, satisfying the conditions of dividing by
    div and is the multiple of mul
    Args:
        div: The number to check whether the number is dividable
        mul: The number to check whether the number is the multiple of mul
        start: The start number for the range
        end: The end number for the range
    Returns: None

    """
    ans = np.array([i for i in range(start, end+1)])
    print(ans[(ans % div == 0) & (ans % mul == 0)])

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5


# code up your solution here
def odd_even_estimator(num_list):
    """
    This program is to estimate how many odd and even numbers in the list and print out the result.
    Args:
        num_list: input, the list containing the numbers we want to estimate
    Returns: None
    """
    num_list = np.array(num_list)
    print('Number of even numbers : {}'. format(np.sum(np.where(num_list % 2 == 0, 1, 0))))
    print('Number of odd numbers : {}'.format(np.sum(np.where(num_list % 2 == 0, 0, 1))))

# 3. Write a Python program which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...


# code up your solution here
def num_estimator():
    """
    This program will print the number between 0 and 50. For the multiple of 3, the program will print fizz instead of
    the number; for the multiple of 5, the program will print buzz instead of the number; for the multiple of both
    3 and 5, the program will print fizzbuzz.
    Returns: None

    """
    for i in range(0, 51):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
def number_finder2(num_list):
    """
    This program will print out the number which is the multiple of 5 but not greater than 150 base on the
    input list.
    Args:
        num_list: input, The list of number to estimate.
    Returns: None

    """
    for i in num_list:
        if i > 150:
            break
        if i % 5 == 0:
            print(i)


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
# Q4
def number_finder3(num_list):
    """
    This is the other version of question four, using range to carry out the estimation
    Args:
        num_list: input, the list of number to estimate
    Returns: None

    """
    for i in range(len(num_list)):
        if num_list[i] > 150:
            break
        elif num_list[i] % 5 == 0:
            print(num_list[i])


# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here
# Q3
def num_estimator2():
    """
    This is the other version of question 3, using comprehension to carry out the estimation
    Returns: None

    """
    for i in range(0, 51): print('fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else 'fizzbuzz' if i % 5 == 0
                                                                                                   and i % 3 == 0 else i)


# 7. Pick one of the questions above and use while loop for a different solution

# code up your solution here
# Q4
def number_finder4(num_list):
    """
    This is the other version of question 4, using while loop to carry out the estimation
    Args:
        num_list: input, the list of number to estimate
    Returns: None

    """
    i = 0
    while num_list[i] <= 150:
        if num_list[i] % 5 == 0:
            print(num_list[i])
        i += 1





