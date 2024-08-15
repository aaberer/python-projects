from random import *

##
## Magic 8 Ball lab for CS 150B.
##
## In this lab, you will work with branching statements.
## 
## @author Andrew Aberer
##         aaberer@colostate.edu
## @version 202102

def get_positive_answer(answer):
    ans = "You may rely on it."
    if answer == 0:
        ans = "As I see it, yes."
    elif answer == 1:
        ans = "Signs point to yes."
    elif answer == 2:
        ans ="Outlook good."
    elif answer == 3:
        ans = "Without a doubt."
    return ans
    
def get_negative_answer(answer):
    ans = ""
    if answer == 0:
        ans = "Don't count on it."
    elif answer == 1:
        ans = "My reply is no."
    elif answer == 2:
        ans ="My sources say no."
    elif answer == 3:
        ans = "Outlook not so good."
    elif answer >= 4:
        ans = "Very doubtful."
    return ans

def get_no_answer(answer):
    ans = "You may rely on it."
    if answer == 0:
        ans = "Reply hazy, try again."
    elif answer == 1:
        ans = "Ask again later."
    elif answer == 2:
        ans = "Better not tello you now."
    elif answer == 3:
        ans = "Cannot predict now."
    elif answer >= 4:
        ans = "Concentrate and ask again."
    return  ans

def getAnswer(category, answer):
    ans = None
    if category < 24:
        ans = get_negative_answer(answer)
    elif category <= 73:
        ans = get_no_answer(answer)
    elif category >= 74:
        ans = get_positive_answer(answer)
    return ans

def printSplash():
    print('88888888888888888888')
    print('8   Magic 8 Ball   8')
    print('8    Ask away      8')
    print('8  Know everything 8')
    print('88888888888888888888')

def run():
    cat = randint(0, 100)
    an = randint(0, 4)
    print(f'category num: {cat} answer num:  {an}')
    print(getAnswer(cat, an))
    print()
    user_input = input('Ask another question (Yes/No?): ')
    if user_input.lower().startswith('n'):
        print('Thank you for playing!')
        return
    print('\nAnd the answer is...\n')
    run() 

if __name__ == '__main__':
    printSplash()
    run()

