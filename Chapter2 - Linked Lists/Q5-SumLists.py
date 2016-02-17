from node import Node

def iterativeReverseSum(head1, head2):
    newList = None
    first = True
    counter = 0
    while head1 != None and head2 != None:
        value = counter + head1.data + head2.data
        counter = 0
        while value > 9:
            value -= 10
            counter +=1
        if first:
            newList = Node(value)
            first = False
        else:
            newList.appendToTail(value)
        head1 = head1.next
        head2 = head2.next
    while head1 != None:
        value = counter + head1.data
        counter = 0
        while value > 9:
            value -= 10
            counter += 1
        newList.appendToTail(value)
        head1 = head1.next
    while head2 != None:
        value = counter + head2.data
        counter = 0
        while value > 9:
            value -= 10
            counter += 1
        newList.appendToTail(value)
        head2 = head2.next
    while counter != 0:
        value = counter
        counter = 0
        while value > 9:
            value -= 10
            counter += 1
        newList.appendToTail(value)
    return newList

def recursiveReverseSum(head1, head2, carry):
    if head1 == None  and head2 == None and carry ==0:
        return None
    value = carry
    if head1 != None:
        value += head1.data
    if head2 != None:
        value += head2.data
    result = Node(value%10)
    if head1 != None or head2 != None:
        more = recursiveReverseSum (None if head1 == None else head1.next, None if head2 == None else head2.next, 1 if value >=10 else 0)
        result.next = more
    return result

class PartialSum():
    def __init__(self):
        self.carry = 0
        self.soma = None

def forwardSum(head1, head2):
    len1 = getLen(head1)
    len2 = getLen(head2)

    if len1 < len2:
        head1 = padList(head1, len2-len1)
    else:
        head2 = padList(head2, len1 - len2)
    soma = forwardSumHelper(head1, head2)
    if soma.carry == 0:
        return soma.soma
    else:
        new = Node(soma.carry)
        new.next = soma.soma
        return new

def forwardSumHelper(head1, head2):
    if head1 == None and head2 == None:
        soma = PartialSum()
        return soma

    soma = forwardSumHelper(head1.next, head2.next)
    value = soma.carry + head1.data + head2.data
    new = Node(value%10)
    new.next = soma.soma

    soma.soma = new
    soma.carry = value/10
    return soma

def padList( node, n):
    head = node
    for i in range(n):
        new = Node(0)
        new.next = head
        head = new
    return head

def getLen(linkedList):
    if linkedList == None:
        return 0
    else:
        return 1 + getLen(linkedList.next)

def main():
    l1 = Node(9)
    l1.appendToTail(7)
    l1.appendToTail(8)
    l2 = Node(6)
    l2.appendToTail(8)
    l2.appendToTail(5)
    print iterativeReverseSum(l1, l2)
    print recursiveReverseSum(l1, l2, 0)
    print  forwardSum(l1, l2)
if __name__ == '__main__':
    main()
