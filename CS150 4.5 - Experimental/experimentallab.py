# -*- coding: utf-8 -*-
"""ExperimentalLab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/CSU-CS150B/handouts/blob/main/Book/Unit2/ExperimentalLab.ipynb

# Lab 4.5 - Practice With Problems

Hi everyone. This is practice with an experimental lab format. For 'saving progress' in this lab, you will want to make sure you have an account setup with google if you are using [colabs](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=9wi5kfGdhK0R) or if you have [downloaded](https://github.com/CSU-CS150B/handouts/tree/main/Book/Unit2) this file, using VS Code (or other local application), you will be fine on your own computer. For those using colabs, make sure you save it to your google drive. 

This lab will take you step by step as you work through the jupyter notebook.

## Task 1: Working With Loops and Strings

For this task, your goal is to write a loop that will reprint the characters of any string. For example:

```
Hello
```

will print to the screen

```
H
e
l
l
o
```

A few things to help you out, remember you can access a specific location in a string using the "indexing" operators `[]` as such, if I wanted to access the first element it would be the following (go ahead and run the code).
"""

print("hello"[0])  # prints h to the screen

## or better done
greeting = "hello"
print(greeting[0])  # prints h to the screen
print(greeting[1])  # prints e to the screen

"""
Another useful reminder is that `len(string)` gives you the total number of characters, so if I wanted to loop the total length of the string, the loop I would setup would be:

```python
loc = 0
while loc < len(greeting):
    # do something
    # make sure to increment loc!
```

Now go ahead and build the loop below! """

greeting = "aloha" #you should change this for testing
loc = 0
while loc < len(greeting):
    print(greeting[loc])
    loc += 1
## put your loop here, and test it using the arrow to the side

"""## Task 2 - Building a reverse string

For this task, you will take the same idea of a loop and "flip it" instead of going from 0 to len(greeting), you will want to set your loc to the *last* index of the string, and count *down* until you are at the first index (0). 

> To think about: if len(string) gives you the entire length, is that the last index or do you need to modify it to get the last index from that?

The other thing to remember is how to concatinate strings. In this case, we are building a string, so in our loop we will want to use a `+=` to the string variable. Run the next code to see an example of that.
"""

example_ans = ""
example_greeting = "aloha"
exloc = 5
while exloc >= 0:
    example_ans += example_greeting[0]
    exloc -= 1
print(example_ans)

# now your turn! 

greeting = "aloha"
ans = ""
loc = 4
while loc > -1:
    print(greeting[loc])
    loc -= 1

## add your loop here - you want answer to eventually be ahola or the reverse of whatever word greeting is set to!


print(ans)

"""## Task 3 - Creating a function

Great, we have figured out how to reverse a string, so now lets build a function so we can continue to do it. As a reminder, a function has the following format

```python
def name(parameters):
    #code - all indented as part of the function block
    #return answer
```

You may want to review functions at this point, and go back to the [functions interactive slides](https://colab.research.google.com/github/CSU-CS150B/handouts/blob/main/Book/Unit1/IntroToFunctions.ipynb) and work on `def nameFormat(first, last):` activity (most the way down the page) as a reminder. 

When you are comfortable, take the code you wrote above, and make it the primary block of the function `reverse_str`. Remember, you want to return the answer not print it here!
"""

# we put in the signature for you, the rest you need to work on
def reverse_str(msg):
    return msg[::-1]

print(reverse_str("aloha"))
print(reverse_str("hello"))

"""## Turning In

If you go to file -> download -> .py, that will allow you to download a python script file built off of this notebook (or export command in vscode). After you download this file, click on the lab link in canvas, and you will be able to upload the lab into zybooks. This lab will also have a quick survey after it, as this is the first time we are trying a jupyter notebook lab for this course, and I am wanting to collect feedback. That is also why this lab only had you build up to one function, instead of building a full program. 

### Future Labs in 163/164
While CS 150B will build you to working on a full program by the end of the semester (we will get there!), I wanted to take a moment about CS 163/4 labs. We alternate theory based labs on Tuesdays and full applications / working programs on Thursdays. If you currently have an A or B in CS 150B, you would do great in the following course which gives you a much stronger programming background! Come talk to me if you are interested in learning more! 


### Extra practice
For the remainder of the lab session, I encourage you to try the extra practice labs in zybooks! Your TAs will guide you to them. Remember, programming takes practice, so it is best you keep at it. 
"""