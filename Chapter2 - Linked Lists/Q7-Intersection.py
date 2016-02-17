from node import Node

def intersection( head1, head2):
    last1 = getLastNode(head1)
    last2 = getLastNode(head2)

    if last1 is not last2:
        return None
    else:
        len1 = getLen(head1)
        len2 = getLen(head2)
        current1 = head1
        current2 = head2
        if len1 > len2:
            for i in range(len1-len2):
                current1 = current1.next
        elif len2 > len1:
            for i in range(len2 - len1):
                current2 = current2.next
        while current1 is not current2:
            current1 = current1.next
            current2 = current2.next
        return current1

def getLastNode( head):
    if head == None:
        return None
    else:
        current = head
        while current.next != None:
            current = current.next
        return current

def getLen(node):
    if node == None:
        return 0
    else:
        return 1 + getLen(node.next)

def main():
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head2 = Node(0)
    head2.next = head1.next.next
    print head1
    print head2
    print intersection(head1,head2)

if __name__ == '__main__':
    main()
