from node import Node

def deleteMiddleNode(middleNode):
    if middleNode == None or middleNode.next == None:
        return False
    current = middleNode
    nextNode = current.next
    current.data = nextNode.data
    current.next = nextNode.next
    del nextNode
    return True


def main():
    head = Node(1)
    head.appendToTail(2)
    head.appendToTail(2)
    head.appendToTail(4)
    head.appendToTail(2)
    head.appendToTail(5)
    head.appendToTail(5)
    head.appendToTail(7)
    head.appendToTail(9)
    print head
    deleteMiddleNode(head.next.next.next.next)
    print head
if __name__ == '__main__':
    main()
