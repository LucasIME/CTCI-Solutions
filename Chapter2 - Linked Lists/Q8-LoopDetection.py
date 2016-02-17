from node import Node

def loopDetection( head):
    slow = head
    fast = head
    colision = None
    while slow != None and fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            colision = slow
            break
    if colision != None:
        start = head
        while start is not colision:
            start = start.next
            colision = colision.next
        return colision
    return None

def main():
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = head1.next
    #print head1
    print loopDetection(head1).data

if __name__ == '__main__':
    main()
