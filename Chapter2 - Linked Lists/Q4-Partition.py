from node import Node

def partition(head, value):
    lesserList = None
    lesserLast = None
    greaterList = None
    greaterLast = None
    current = head
    while current != None:
        if current.data < value:
            if lesserList == None:
                lesserList = current
                lesserLast = lesserList
            else:
                lesserLast.next = current
                lesserLast = lesserLast.next
        else:
            if greaterList == None:
                greaterList = current
                greaterLast = greaterList
            else:
                greaterLast.next = current
                greaterLast = greaterLast.next
        current = current.next
    if lesserLast != None:
        lesserLast.next = greaterList
    if greaterLast != None:
        greaterLast.next = None

def main():
    head = Node(3)
    head.appendToTail(5)
    head.appendToTail(8)
    head.appendToTail(5)
    head.appendToTail(10)
    head.appendToTail(2)
    head.appendToTail(1)
    print head
    partition(head, 5)
    print head
if __name__ == '__main__':
    main()
