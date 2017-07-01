'''
Write a function that rotates a list by k elements. 
For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
Try solving this without creating a copy of the list.
----------------------------------------------------
Input: Two arguments. List of elements and positive integer
Output: Converter list of elements
----------------------------------------------------
Example:
rotate_list([1, 2, 3, 4, 5, 6], 2) === [3, 4, 5, 6, 1, 2]
rotate_list([1, 2, 3, 4, 5, 6], 3) === [4, 5, 6, 1, 2, 3]
'''

def rotate_list(elements, rotates):
    for i in range(1,rotates+1):
        list.append(elements,i)
    elements=elements[rotates:]
    
    return elements

if __name__ == '__main__':
    assert rotate_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2], "First"
    assert rotate_list([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3], "Second"
    assert rotate_list([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6], "Third"

    print("All set? Click \"Check\" to review your code and earn rewards!")
    
    #elements = [1, 2, 3, 4, 5, 6]
    #rotates = 3
    
    #for i in range(1,rotates+1):
        #list.append(elements,i)
    #elements=elements[rotates:]
    #print (elements)
