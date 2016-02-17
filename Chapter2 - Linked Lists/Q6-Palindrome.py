from node import Node

def isPal(head, length):
    if head == None:
        return False
    stack = []
    current = head
    for i in range(length/2):
        stack.append(current.data)
        current = current.next
    if length%2 == 1:
        current = current.next
    for i in range(length/2):
        value = stack.pop()
        if value != current.data:
            return False
        current = current.next
    return True


def getLen(linkedList):
    if linkedList == None:
        return 0
    else:
        return 1 + getLen(linkedList.next)

def main():
    head = Node(1)
    head.appendToTail(2)
    head.appendToTail(3)
    head.appendToTail(2)
    head.appendToTail(1)
   # head.appendToTail(4)
   # head.appendToTail(2)
   # head.appendToTail(5)
   # head.appendToTail(5)
   # head.appendToTail(7)
   # head.appendToTail(9)
    print head
    print isPal(head, getLen(head))
if __name__ == '__main__':
    main()
