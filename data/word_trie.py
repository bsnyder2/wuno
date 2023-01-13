class Node:
    def __init__(self, letter):
        self.LETTER = letter
        # associates letters and nodes
        self.children = {}


class WordTrie:
    def __init__(self):
        self.ROOT = Node("")

    def insert(self, word):
        cur_node = self.ROOT

        for letter in word:
            # if no branch to next letter
            if letter not in cur_node.children:
                # create new node with next letter
                cur_node.children[letter] = Node(letter)
            # move down to next letter
            cur_node = cur_node.children[letter]

    def continuant_letters(self, word):
        cur_node = self.ROOT

        for letter in word:
            if letter not in cur_node.children:
                return set()
            cur_node = cur_node.children[letter]
        return set(cur_node.children.keys())