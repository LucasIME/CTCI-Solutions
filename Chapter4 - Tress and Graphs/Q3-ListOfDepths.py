from node import *

def listOfDepths(root):
    q = []
    s = set()
    resp = {}
    q.append( (root, 0) )
    while len(q) > 0:
        currNode, currLevel = q.pop()
        if currNode not in s:
            s.add(currNode)
            if currLevel not in resp:
                resp[currLevel] = [currNode.data]
            else:
                resp[currLevel].append(currNode.data)
            for node in currNode.children:
                q.insert(0, (node, currLevel+1) )
    return resp


def main():
    a = Node(1)
    a.children.append( Node(2))
    a.children.append(Node(3))
    a.children[0].children.append(Node(4))
    a.children[1].children.append(Node(5))
    a.children[0].children[0].children.append(Node(6))
    print listOfDepths(a)
if __name__ == '__main__':
    main()
