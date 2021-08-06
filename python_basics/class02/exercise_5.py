'''
Edit this file to complete Exercise 5
'''

# 1. rite a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here

i = 1500
divBy_5and7 = []

while i <= 2700:
    if i % 7 == 0 and i % 5 == 0:
        divBy_5and7.append(i)
    i += 1
    
print(divBy_5and7)



# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here

nums = [1,2,3,4,5,...]
odds = 0
evens = 0

for i in nums:
    if i % 2 == 0:
        evens += 1
    else: 
        odds += 1

print('Number of odd numbers: {}'.format(odds))
print('Number of even numbers: {}'.format(evens))



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

a = 0

while a <= 50:
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz')
    elif a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print('{}'.format(a))
    a += 1



# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here

list1 = [5,7,24,335,74,15,33,...]
list1.sort()

for i in list1:
    if i % 5 == 0 and i <= 150:
        print(i)


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here

# Q4
for i in range(len(list1)):
    if list1[i] % 5 == 0 and list1[i] <= 150:
        print(list1[i])


# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here

# Q4
print([i for i in list1 if i % 5 == 0 and i <= 150])


# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here

i = 0
while i < len(list1):
    if list1[i] % 5 == 0 and list1[i] <= 150:
        print(list1[i])
    i += 1
