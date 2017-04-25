class BiNode:
    def __init__(self, data):
        self.node1 = None
        self.node2 = None
        self.data = data

    def __repr__(self):
        out = ""
        node = self
        while node != None:
        #out = str(self.node1) + "<-" +  str(self.data) + "->" + str(self.node2)
            out += str(node.data) + "->"
            node = node.node2
        return out

def convertToLL(head):
    if head is None:
        return (None, None)
    startLeft, endLeft = convertToLL(head.node1)
    startRight, endRight = convertToLL(head.node2)

    head.node1 = endLeft
    if endLeft != None:
        endLeft.node2 = head
    head.node2 = startRight
    if startRight != None:
        startRight.node1 = head

    listhead = head if startLeft is None else startLeft
    listend = head if endRight is None else endRight

    return (listhead, listend)

def main():
    head = BiNode(4)
    head.node1 = BiNode(2)
    head.node2 = BiNode(5)
    head.node2.node2 = BiNode(6)
    head.node1.node2 = BiNode(3)
    head.node1.node1 = BiNode(1)
    head.node1.node1.node1 = BiNode(0)

    listStart, listEnd = convertToLL(head)
    print(listStart)

main()