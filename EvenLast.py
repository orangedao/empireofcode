'''You are given an array of integers. 
You should find the sum of the elements with even indexes (0th, 2nd, 4th...) 
then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.
----------------------------------------------------------
For an empty array, the result will always be 0 (zero).

Input: A list of integers.
Output: The number as an integer.

Example:
even_last([0, 1, 2, 3, 4, 5]) == 30
even_last([1, 3, 5]) == 30
even_last([6]) == 36
even_last([]) == 0

Precondition:
0 ≤ |array| ≤ 20
How it is used:

Indexes and slices are important elements of coding in python and other languages. 
This will come in handy down the road!
'''


def even_last(array):
    if len(array) == 0:
        res_array = 0
    else:
        array_new = array[::2]
        res_array = sum(array_new) * array[-1]
    
    return res_array


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"

    print("Use 'Check' to earn sweet rewards!")
        

