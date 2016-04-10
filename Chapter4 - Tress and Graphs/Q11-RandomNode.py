from node import *

class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size  = 1
    def find(self, data):
        node = self
        while node != None:
            if node.data == data:
                return node
            elif node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
        return None

    def insertInOrder(self, data):
        if data <= self.data:
            if self.left == None:
                self.left =  BinaryTree(data)
            else:
                self.left.insertInOrder(data)
        else:
            if self.right == None:
                self.right = BinaryTree(data)
            else:
                self.right.insertInOrder(data)
        self.size+=1
        
    def delete(self, data):
        pass
    def getRandomNode(self):
        import random
        leftSize = 0 if self.left == None else self.left.size
        index = random.randrange(0, self.size, 1)
        if index < leftSize:
            return self.left.getRandomNode()
        elif index == leftSize:
            return self
        else:
            return self.right.getRandomNode()
    def __repr__(self):
        return str(self.data)

def main():
    a = BinaryTree(20)
    a.insertInOrder(10)
    a.insertInOrder(5)
    a.insertInOrder(15)
    a.insertInOrder(25)
    a.insertInOrder(1.5)
    a.insertInOrder(3)
    a.insertInOrder(50)
    a.insertInOrder(20)
    a.insertInOrder(70)
    a.insertInOrder(65)
    a.insertInOrder(7)
    #a.left = BNode(10)
    #a.left.left = BNode(5)
    #a.left.right = BNode(15)
    #a.right = BNode(25)
    #a.right.left = BNode(1.5)
    #a.right.right = BNode(3)
    #b = BNode(50)
    #b.left = BNode(20)
    #b.left.left = BNode(10)
    #b.left.left.left = BNode(5)
    #b.left.left.right = BNode(15)
    #b.left.right = BNode(25)
    #b.right = BNode(60)
    #b.right.right = BNode(70)
    #b.right.right.left = BNode(65)
    #b.right.right.right = BNode(80)
    print a
    for i in range(15):
        print a.getRandomNode()
if __name__ == '__main__':
    main()
