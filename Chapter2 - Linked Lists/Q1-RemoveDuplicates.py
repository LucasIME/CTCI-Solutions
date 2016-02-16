from node import Node

def removeDuplicates(head):
    d = {}
    no = head
    d[no.data] =  True
    while no.next != None:
        if no.next.data not in d:
            d[no.next.data] = True
            no = no.next
        else:
            no.next = no.next.next

def removeDuplicatesNoExtraMemory(head):
    current = head
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next



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
    removeDuplicates(head)
    print head
if __name__ == '__main__':
    main()
