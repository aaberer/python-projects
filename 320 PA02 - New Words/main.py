# extract values from a sorted list

import math  # optional and you can delete this line if not useful

# subroutines if any, go here


# your subroutine goes here
def new_words(words, wordlist):
    if words is None:
        return None
    if wordlist is None:
        return None
    if type_check(words) is False:
        return None
    if type_check(wordlist) is False:
        return None
    wordsSorted = sorted(words, key=str.casefold)
    wordsSortedArray = list(word.lower() for word in wordsSorted)

    worlistArray = list(word.lower() for word in wordlist)

    result = []
    for word in wordsSortedArray:
        if word not in worlistArray:
            result.append(word)
    return tuple(result)


def type_check(check):
    if type(check) is tuple:
        return True
    else:
        return False
