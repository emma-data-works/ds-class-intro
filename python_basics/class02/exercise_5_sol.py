'''
Edit this file to complete Exercise 5
'''

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
def sol1():

    # get input list, create storage
    in_lst = range( 1500, 2701)
    out_lst = []

    # loop to filter the correct answer
    for i in in_lst:
        if (i%7==0) and ( i%5==0):
            out_lst.append(i)

    return out_lst

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
def sol2( ):
    '''
    Though this might not match the coding request,
    I will add the var numbers inside the function
    for the purpose of testing 
    '''
    # input numbers 
    in_lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # create odd list, even list
    odd_lst, even_lst = [], []

    # loop to filter the correct answer
    for i in in_lst: 
        if i % 2:
            odd_lst.append(i)
        else:
            even_lst.append(i)
    
    return odd_lst, even_lst


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
def sol3( ):

    # integers from 0 to 50 
    in_lst = range( 0, 51)

    # loop to filter the correct answer
    for i in in_lst:
        if i % 3 == 0:
            if i % 5 == 0:
                print( 'fizzbuzz')
            else:
                print( 'fizz')
        elif i % 5 == 0:
            print( 'buzz')

# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
def sol4( ):
    '''
    Like sol2,  the input is hardwired in the function
    '''
    in_lst = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

    # create storage
    out_lst = []

    # loop to filter the correct answer
    for i in in_lst: 
        if i > 150:
            break
        if i % 5 == 0:
            out_lst.append( i)
    
    return out_lst
        
# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
def sol5():
    '''
    sol1 variant 
    '''

    # get input list, create storage
    in_lst = range( 1500, 2701)
    out_lst = []

    # loop to filter the correct answer
    for x in range(len(in_lst)):
        i = in_lst[x] # obtain the element in the list 
        if (i%7==0) and ( i%5==0):
            out_lst.append(i)

    return out_lst


# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here
def sol6():
    '''
    sol4 variant
    '''

    in_lst = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

    def sol4( i):
        if (i <= 150) and i % 5 ==0:
            return i

    out_lst = [ x for x in map( sol4, in_lst) if x is not None] 

    return out_lst



# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here
def sol7( ): 
    '''
    sol3 variant
    '''

    # define filter
    def filter( x):
        if x % 3 == 0:
            if x % 5 == 0:
                print( 'fizzbuzz')
            else:
                print( 'fizz')
        elif x % 5 == 0:
            print( 'buzz')

    # integers from 0 to 50 
    in_lst = range( 0, 51)

    # loop to filter the correct answer
    done = False
    i = 0 
    while not done: 

        # main function 
        filter( in_lst[i])

        # update counter
        i += 1 

        # check termination
        if i == len(in_lst):
            done = True 

if __name__ == '__main__':

    # Run and test my code 
    cmp_lst = [ (sol1, sol5), ( sol4, sol6), ( sol3, sol7), [sol2]]
    texts   = [ ('sol1', 'sol5'), ('sol4', 'sol6'), ('sol3', 'sol7'), ('sol2')]

    for fn_set, txt_set in zip(cmp_lst, texts):
        for fn, txt in zip( fn_set, txt_set):
            print( f'\n{txt}:\n')
            print( f' {fn.__call__()}')

