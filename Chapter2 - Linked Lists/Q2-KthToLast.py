from node import Node

def knowingSizeKLast(head, k):
    n = 0
    current = head
    while current != None:
        n+=1
        current = current.next
    if k > n:
        return head
    current = head
    counter = 1
    while counter != n-k+1:
        current = current.next
        counter+=1
    return current

def iterativeKLast(head, k):
    p1 = head
    p2 = head
    for i in range(k):
        if p2 == None:
            print "Out of Bounds"
            return None
        p2 = p2.next
    while p2 != None:
        p2 = p2.next
        p1 = p1.next
    return p1

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
    print iterativeKLast(head, 3)
    print knowingSizeKLast(head, 3)
if __name__ == '__main__':
    main()
