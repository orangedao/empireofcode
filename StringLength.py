'''Define a function that computes the length of a given string.
-------------------
Input: String.
Output: It's length.
--------------------
Example:

str_length("") == 0
str_length("mo") == 2
str_length("length") == 6
'''

def str_length(line):
    
    
    return len(line)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert str_length("") == 0, "1st example";
    assert str_length("mo") == 2, "2st example";
    assert str_length("length") == 6, "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
    
    #line = 'Code\'s finished?'
    

