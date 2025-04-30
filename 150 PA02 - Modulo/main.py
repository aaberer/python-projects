##
# Modulo lab for CS 150B.
##
# In this lab, you will get practice using while loops and modulos.
##
# @author Abdrew Aberer
# aaberer@colostate.edu
# @version 202102

def factorial(num1):
    total = 1
    while (num1 > 0):
        total = total * num1
        num1 -= 1
    return total


def moduloPractice(num1):
    num1 = num1 % 9
    return num1


def evenNum(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    return


def oddNum(num1):
    if num1 % 2 == 1:
        return True
    else:
        return False
    return


def checkNum(num1):
    if num1 % 2 == 0:
        return 'Even'
    elif num1 % 2 == 1:
        return 'Odd'
    return


def run():
    num1 = int(input())
    print("Factorial:", factorial(num1))
    print("Modulo:", moduloPractice(num1))
    print("Even:", evenNum(num1))
    print("Odd:", oddNum(num1))
    print("Even or Odd:", checkNum(num1))


if __name__ == '__main__':
    print()
    run()
