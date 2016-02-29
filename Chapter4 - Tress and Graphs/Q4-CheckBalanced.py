from node import *

def isBalanced(root):
    if checkHeight(root) == -1:
        return False
    else:
        return True

def checkHeight(root):
    if root == None:
        return 0
    leftHeight = checkHeight(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = checkHeight(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) +1
def main():
    a = BNode(1)
    a.left = BNode(2)
    a.right  = BNode(3)
   # a.left.left = BNode(4)
    #a.left.left.left = BNode(5)
    #a.left.righ = BNode(6)
    #a.right.right = BNode(7)
    print isBalanced(a)
if __name__ == '__main__':
    main()
