class Node:
    def __init__(self, data):
        self.DATA = data
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

    def longer_possible(self, word):
        cur_node = self.ROOT

        for letter in word:
            if letter not in cur_node.children:
                return False
            cur_node = cur_node.children[letter]
        return len(cur_node.children) > 0
