from node import *

def minTree(v):
    if v == []:
        return None
    head = Node(v[len(v)//2])
    left = minTree(v[:len(v)//2])
    right = minTree(v[len(v)//2 +1:])
    if left != None:
        head.children.append(left)
    if right != None:
        head.children.append(right)
    return head


def main():
    v  = [ 2, 3, 5, 10, 15, 20, 30, 40, 100, 240, 500]
    t = minTree(v)
    #print t
if __name__ == '__main__':
    main()
