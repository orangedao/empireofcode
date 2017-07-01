'''
Define a function that takes two numbers as arguments and returns the largest of them.
-----------------
Input: Two arguments as numbers.
Output: Maximum of two.
-----------------
Example:

my_max(3, 3) == 3
my_max(0, 1) == 1
my_max(3, 2) == 3
'''

def my_max(a, b):
    if a>b:
        return a
    else:
        return b
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    #return a

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert my_max(3, 3) == 3, "First"
    assert my_max(0, 1) == 1, "Second"
    assert my_max(3, 2) == 3, "Third"

    print("All set? Click \"Check\" to review your code and earn rewards!")
    #a=500
    #b=90
    #print (my_max(a, b))
