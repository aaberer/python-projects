##  Andrew Aberer | aaberer@colostate.edu
'''
#https://www.cs.colostate.edu/~cs150b/labs/lab06
method 1: makelist()
'''
from ssl import _create_default_https_context
from typing import final


def makelist(number):
    newlist = []
    for i in range(number):
        newlist.append(i)
    return newlist


'''
method 2 - rocketcountdown()
param - int (the number used to count down from)
return string
'''
'''
STUDENT TODO METHOD 2
'''
def rocketcountdown(countdown):
    countdownlist = []
    x = countdown
    for countdown in range(countdown):
        countdownlist.append(x)
        x -= 1
    countdownlist.append("We have lift off!")
    return countdownlist

'''
method 3 - doubleloop()
params - 2 ints one for a loop length and the other is the multiplier
return a list
'''
'''
STUDENT TODO METHOD 3
'''
def doubleloop(len1,len2):
    doublelooplist = []
    x = len1
    y = len2
    for x in range(len1):
        for y in range(len2):
            doublelooplist.append('{}:{}'.format(x, y))
    return doublelooplist

'''
method 4: howmanycombos()
params- 3 integers representing the code to unlock a padlock
returns - a list of all possible combinations
'''
'''
STUDENT TODO METHOD 4
'''
def howmanycombos(l1, l2, l3):
    howmanycomboslist = []
    for x in range(l1 + 1):
        for y in range (l2 + 1):
            for z in range (l3 +1):
                howmanycomboslist.append('{},{},{}'.format(x, y, z))
    return howmanycomboslist


'''
cansofpop()
params
    number - total number of pops
    takedown - interval of how many pops to take down
'''
'''
STUDENT TODO METHOD 5
'''
def cansofpop(number, takedown):
    cansofpoplist = []
    x = number
    new = number
    while x > 0 and takedown < x:
        new = x - takedown
        cansofpoplist.append('{0} cans of pop on the wall {0} cans of pop, take {1} down and pass them around, {2} cans of pop on the wall'.format(x, takedown, new))
        x -= takedown
    else:
        takedown = x
        new = x - takedown
        cansofpoplist.append('{0} cans of pop on the wall {0} cans of pop, take {1} down and pass them around, {2} cans of pop on the wall'.format(x, takedown, new))
        x -= takedown
        cansofpoplist.append('All cans of pop are gone!')
    return cansofpoplist


def main():
    print(makelist(10))
    print(rocketcountdown(10))
    print(doubleloop(2, 2))
    print(howmanycombos(1, 2, 1))
    print(cansofpop(3, 1))
    '''
    This is where you can write your own tests for your methods!
    '''


if __name__ == '__main__':
    main()
