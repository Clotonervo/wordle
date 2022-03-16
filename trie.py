class TrieNode(object):

    def __init__(self, char):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1

    def add(self, root, word):
        node = root
        for letter in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == letter:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(letter)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
            # Everything finished. Mark it as the end of a word.
        node.word_finished = True