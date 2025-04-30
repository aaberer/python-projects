from main import Trie


# Tree used for all the tests.
myTree = Trie(True)

# Tuple of words to add
myTuple = tuple(["disintegrate", "kill", "death", "Murder", "dishonor", "decapitate", "defrost", "desfigure"])

# test 1: adding to the tree succesfully and finding
assert(myTree.add("defrost") == True)
assert(myTree.find("defrost") == True)

# test 2: adding another word that should overlap
assert(myTree.add("desfigure") == True)
assert(myTree.find("desfigure") == True)


# test 3: trying to add a word that is already in the tree
assert(myTree.add("defrost") == False)

# test 4: adding a tuple of words, which contain 2 words that are already in the tree
assert(myTree.add_keys(myTuple) == 6)
assert(myTree.find("decapitate") == True)

# test 5: Making sure prefixes are incorrect words, then adding a word that is a prefix to some words
assert(myTree.find("des") == False)
assert(myTree.add("des") == True)
assert(myTree.add("des") == False)
assert(myTree.find("des") == True)

# test 6: Removing a word that doesn't exist in the tree
assert(myTree.remove("Bomba") == False)

# test 7: Removing a word that is a prefix and checking the other words still exist
assert(myTree.remove("des") == True)
assert(myTree.find("des") == False)
assert(myTree.find("desfigure") == True)

# test 8: Removing a word that is not a prefix to another word
assert(myTree.remove("desfigure") == True)
assert(myTree.find("desfigure") == False)
assert(myTree.find("decapitate") == True)

# test 9: prefix testing
all_Words = myTree.partial("d")
assert (len(all_Words) == 5) 

# test 10: prefix empty string (edge case)
all_Words = myTree.partial("")

assert (len(all_Words) == 7) 


# test 11: add argument test
assert(myTree.add(None) == False)
assert(myTree.add("") == False)

# test 12: remove argument test
assert(myTree.remove(None) == False)
assert(myTree.remove("") == False)

# test 13: find argument test
assert(myTree.find(None) == False)
assert(myTree.find("") == False)

# test 14: add_keys argument test
assert(myTree.add_keys(None) == False)
assert(myTree.add_keys(tuple()) == 0)

# test 15: Partial argument test
assert(myTree.partial(None) == set())

# test 16: edge case for add_keys()
assert(myTree.add_keys(tuple([None, "", None, "Defamation"])) == 1)
assert(myTree.add("一生懸命") == True)
assert(myTree.find("一生懸命") == True)