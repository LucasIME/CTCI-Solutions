from node import *

def checkSubtree( tree1, tree2):
    if getPreOrder(tree2) in getPreOrder(tree1) and getInOrder(tree2) in getInOrder(tree1):
        return True
    else:
        return False

def getPreOrder(head):
    resp = []
    preOrder(head, resp)
    return ''.join(resp)

def preOrder(head, resp):
    if head == None:
        resp.append('n')
        return
    resp.append(str(head.data))
    preOrder(head.left, resp)
    preOrder(head.right, resp)

def getInOrder(head):
    resp = []
    inOrder(head, resp)
    return ''.join(resp)

def inOrder(head, resp):
    if head == None:
        resp.append('n')
        return
    inOrder(head.left, resp)
    resp.append(str(head.data))
    inOrder(head.right, resp)

def checkSubtree2(tree1, tree2):
    if tree2 == None:
        return True
    return subTree(tree1, tree2)

def subTree(tree1, tree2):
    if tree1 == None:
        return False
    elif tree1.data == tree2.data and matchTree(tree1, tree2):
        return True
    return subTree(tree1.left, tree2) or subTree(tree1.right, tree2)

def matchTree(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    elif tree1 == None or tree2 == None:
        return False
    elif tree1.data != tree2.data:
        return False
    else:
        return matchTree(tree1.left, tree2.left) and matchTree(tree1.right, tree2.right)

def main():
    a = BNode(20)
    a.left = BNode(10)
    a.left.left = BNode(5)
    a.left.right = BNode(15)
    a.right = BNode(25)
    #a.right.left = BNode(1.5)
    #a.right.right = BNode(3)
    b = BNode(50)
    b.left = BNode(20)
    b.left.left = BNode(10)
    b.left.left.left = BNode(5)
    b.left.left.right = BNode(15)
    b.left.right = BNode(25)
    b.right = BNode(60)
    b.right.right = BNode(70)
    b.right.right.left = BNode(65)
    b.right.right.right = BNode(80)
    print checkSubtree(b, a)
    print checkSubtree2(b, a)
if __name__ == '__main__':
    main()
