# Determine if a tuple can be made into a palindrome by removing exactly one element

# An example import. Delete or replace as desired. Be careful with what libraries you use:
# Non-default python libraries may not work in Zybooks.
import math 

# Subroutines if any, go here


# Fill in find_palindrome
# IF ALREADY A PALINDROME STILL HAVE TO CHECK REMOVAL
# Goal is O(n)
def find_palindrome(pattern):
    # if pattern length < 2 return None
    # if pattern = null return None
    # loop trough pattern removing one tuple
    #   passing to is_palindrome to check
    #       if found return tuple
    #       else return None
    if type_check(pattern) is False:
        return None

    if len(pattern) <= 2:
        return None
    
    if pattern is None:
        return None
    
    for i in range(len(pattern)):
        shift_pattern = pattern[:i] + pattern[i + 1:]
        if is_palindrome(shift_pattern):
            return shift_pattern

    return None


def type_check(check):
    if type(check) is tuple:
        return True
    else:
        return False


# t[start:end] result tuple starting with t[start] and ending with t[end-1].
# increment t[start:end:2] selects every other element of the list, beginning with start
# for e in reverse(t): iterator like range and does not actually reverse the values in t
def is_palindrome(pattern): 
    if pattern is None:
        return False
    else:
        return pattern == pattern[::-1]
