'''
Given a string, return a new string where the first and last chars have been exchanged.
------------------------------------
Input: String.
Output: Changed string.
------------------------------------
Example:

sym_exchange("az") === "za"
sym_exchange("aiiiiiz") === "ziiiiia"
sym_exchange("length") === "hengtl"
'''
def symb_exchange(line):
    lst = list(line)
    lst[0],lst[-1]=lst[-1],lst[0]
    line=''.join(lst)
   
    return line

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert symb_exchange("az") == "za", "1st example";
    assert symb_exchange("aiiiiiz") == "ziiiiia", "2st example";
    assert symb_exchange("length") == "hengtl", "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
    
    #line0 = "aiiiiiz"
    #print(symb_exchange(line0))
    #lst = list(line0)
    #lst[0],lst[-1]=lst[-1],lst[0]
    #line=''.join(lst)
    #print(lst)
    #print(line)
    
