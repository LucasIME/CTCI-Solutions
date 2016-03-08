from node import *

class BNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    def addLeft(self, data):
        node = BNode(data)
        self.left = node
        node.parent = self

    def addRight(self, data):
        node = BNode(data)
        self.right = node
        node.parent = self
    def __repr__(self):
        return str(self.data)
def getSucessor(node):
    if node == None:
        return None
    if node.right != None:
        return getLeftMostChild(node.right)
    else:
        while node.parent != None and node == node.parent.right:
            node = node.parent
        return node.parent
def getLeftMostChild(node):
    if node == None:
        return None
    while node.left != None:
        node = node.left
    return node

def main():
    a = BNode(1)
    a.addLeft(0)
    a.addRight(3)
    a.left.addLeft(-2)
    a.left.left.addLeft(-5)
    a.left.addRight(0.5)
    a.right.addRight(7)
    print getSucessor(a.left.right)
if __name__ == '__main__':
    main()
