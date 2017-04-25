class Trie:
    def __init__(self, wordList):
        self.root = {}
        self.end = '_end_'
        for word in wordList:
            self.add(word)

    def add(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end] = self.end

    def containsWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        if self.end in node:
            return True
        return False

def getLongest(words):
    trie = Trie(words)
    resp = ""
    for word in words:
        if isMadeOfOthers(word, trie):
            if len(word) > len(resp):
                resp = word
    return resp

def isMadeOfOthers(word, trie):
    node = trie.root
    for i, letter in enumerate(word):
        if letter not in node:
            return False
        node = node[letter]
        if trie.end in node:
            if isMadeOfOthers(word[i+1:], trie) or trie.containsWord(word[i+1:]):
                return True
    return False

def main():
    words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker', 'giantwordthatisntomadeofothers']
    print(getLongest(words))

main()