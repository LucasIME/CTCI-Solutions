from node import *

def getLCA(head, n1, n2):
    if ( not find(head, n1) or not find(head, n2)):
        return None
    else:
       return getactualLCA(head, n1, n2)

def getactualLCA(head, n1, n2):
    if head == None:
        return None
    elif head.data == n1:
        return head
    elif head.data == n2:
        return head
    n1inLeft = find(head.left, n1)
    n2inLeft = find(head.left, n2)
    if n1inLeft != n2inLeft:
        return head
    childSide = head.left if n1inLeft else head.right
    return getactualLCA(childSide, n1, n2)

def find(head, h1):
    if head == None:
        return False
    if h1== head.data:
        return True
    return find(head.left, h1) or find(head.right, h1)
def main():
    a = BNode(1)
    a.left = BNode(0)
    a.right = BNode(2)
    a.right.left = BNode(1.5)
    a.right.right = BNode(3)
    print getLCA(a, 0, 3)
if __name__ == '__main__':
    main()
