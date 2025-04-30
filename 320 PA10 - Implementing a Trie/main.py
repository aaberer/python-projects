class Trie:
    def __init__(self, is_word=False):
        if not self:
            return None
        if self is None:
            return None
        if is_word is None:
            return None

        self.child = {}
        self.wordEnd = is_word

    def add(self, key: str) -> bool:
        if not key:
            return False
        if key is None:
            return False
        if key == "":
            return False

        curr = self
        for char in key:
            if char not in curr.child:
                curr.child[char] = Trie(is_word=False)
            curr = curr.child[char]

        if not curr.wordEnd:
            curr.wordEnd = True
            return True
        else:
            return False

    def add_keys(self, keys: tuple[str, ...]) -> int:
        if not keys:
            return 0
        if keys is None:
            return 0

        count = 0
        for word in keys:
            if word is None:
                continue
            if word == "":
                continue
            if word is not None and self.add(word):
                count += 1

        return count

    def remove(self, key: str) -> bool:
        if not key:
            return False

        def remove_helper(node, key, depth=0):
            if depth == len(key):
                if not node.wordEnd:
                    return False

                node.wordEnd = False

                return len(node.child) == 0

            char = key[depth]
            if char not in node.child:
                return False

            can_delete_child = remove_helper(node.child[char], key, depth + 1)
            if can_delete_child:
                del node.child[char]
                return len(node.child) == 0 and not node.wordEnd

            return False

        return remove_helper(self, key)

    def find(self, key: str) -> bool:
        if not key:
            return False
        if key is None:
            return False
        if key == "":
            return False

        curr = self
        for char in key:
            if char not in curr.child:
                return False
            curr = curr.child[char]

        return curr.wordEnd

    def partial(self, prefix: str) -> set[str]:
        if not prefix:
            return set()
        if prefix == "":
            return self.get_all_words()

        curr = self
        for char in prefix:
            if char not in curr.child:
                return set()
            curr = curr.child[char]

        result = set()
        self.get_words(curr, prefix, result)
        return result

    def get_words(self, node, prefix, result):
        result = set()
        if node.wordEnd:
            result.add(prefix)

        for char, child_node in node.child.items():
            result.update(self.get_words(child_node, prefix + char, result))

        return result

    def get_all_words(self):
        result = set()
        self.get_words(self, "", result)
        return result
