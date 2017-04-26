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


def multiSearch(t, b):
    trie = Trie(t)
    node = trie.root
    resp = []
    for i in range(len(b)):
        substr = b[i:]
        node = trie.root
        for j, letter in enumerate(substr):
            if letter not in node:
                break
            node = node[letter]
            if trie.end in node:
                resp.append((substr[:j+1], i))
    return resp

def main():
    T = ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']
    b = 'mississippi'
    print(multiSearch(T, b))

main()