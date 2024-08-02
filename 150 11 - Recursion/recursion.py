#   Andrew Aberer aaberer@colostate.edu
#https://www.cs.colostate.edu/~cs150b/labs/lab11
## Simple countdown loop
## prints out from n to 0, one number on each line. 
## use a recursive solution to the loop! not a loop!
## Student TODO - where do you place the print statement in the function?
def countdown(n):
    print(n)
    if n == 0:
        return
    countdown(n-1)
    
## Simple countup loop
## prints out from 1 to n, one number on each line. 
## Use the algorithm for countdown, but change the line of the print, along with function name!
def countup(n):
    if n == 0:
        return
    countup(n-1)
    print(n)

# Factorial - Uses recursion to return the factorial of  the number
# Reminder factorial 3 is 6 (3! = 3 * 2 * 1)
# parameter - n a single int value
# returns the factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# string_reverse(s)
# params: s which is a single string
# returns: The parameter string in reverse order.
def string_reverse(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + string_reverse(s[:-1])

#build_reverse_list(n)
# paremeter - n a single int value
# returns a list of numbers from n to 0
def build_reverse_list(n):
    lst = [n]
    if n == 0:
        return [0]
    else:
        return lst + build_reverse_list(n-1)

# even_odd_list(values)
# paremeter - values is a list of numbers
# returns a list with 'even' or 'odd' for each number in the list
def even_odd_list(values):
    lst = []
    if len(values) == 0:
        return lst
    if values[0] % 2 == 1:
        lst.append('Odd')
    else:
        lst.append('Even')
    return lst + even_odd_list(values[1:])       

def main():
   print("Uncomment blocks of code as you develop the functions for testing")
   print("Counting down from 6")
   countdown(6)
   print("Counting up from 5")
   countup(5) 
   print("Factorial of 10 is", factorial(10))
   print("Testing reverse", string_reverse('!siht tog uoy'))
   print("Testing string reverse", string_reverse('ytisrevinU etatS odaroloC'))
   print("Testing build reverse list", build_reverse_list(6))
   print("Testing even odd list", even_odd_list([17, 22, 42, 3, 14, 16, 0]))


if __name__ == '__main__':
    main()

