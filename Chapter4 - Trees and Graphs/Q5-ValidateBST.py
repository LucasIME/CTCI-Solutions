from node import *

def isBST(root, minV, maxV):
    if root == None:
        return True
    else:
        if root.data >= minV and root.data <= maxV:
            return isBST(root.left, minV, root.data) and isBST(root.right, root.data, maxV)
        else:
            return False

def main():
    a = BNode(1)
    a.left = BNode(0)
    a.right  = BNode(3)
    a.left.left = BNode(-2)
    a.left.left.left = BNode(-5)
    a.left.right = BNode(0.5)
    a.right.right = BNode(7)
    print isBST(a, float('-inf'), float('inf'))
if __name__ == '__main__':
    main()
