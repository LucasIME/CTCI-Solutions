class Node():
    def __init__(self, key, v):
        self.key = key
        self.v = v
        self.left = None
        self.right = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, key, value):
        if self.head == None:
            self.head = Node(key, value)
            self.tail = self.head
            return self.head
        newNode = Node(key, value)
        self.tail.right = newNode
        newNode.left = self.tail
        self.tail = newNode
        return newNode

    def __repr__(self):
        resp = ""
        no = self.head
        while no.right != None:
            resp += str(str(no.key) + '/' + str(no.v)) + ' -> '
            no = no.right
            resp += str(str(no.key) + '/' + str(no.v))
        return resp
    
class Cache():
    def __init__(self, size):
        self.size = size
        self.hmap = {}
        self.llist = LinkedList()
        for i in range(size):
            self.hmap[i] = self.llist.add(i, '')  

    def add(self, key, value):
        if key not in self.hmap:
            node = self.llist.tail
            del self.hmap[node.key]
            node.key = key
            node.v = value
            #print(node, node.left, node.right, node.key, node.v)
            node.left.right = None
            self.llist.tail = node.left
            node.left = None
            node.right = self.llist.head
            self.llist.head.left = node
            self.llist.head = node
            self.hmap[key] = node
            
        else:
            node = self.hmap[key]
            if node == self.llist.head:
                node.v = value
            elif node == self.llist.tail:
                node.left.right = None
                self.llist.tail = node.left
                node.left = None
                node.right = self.llist.head
                self.llist.head.left = node
                self.llist.head = node
                node.v = value
            else:
                node.left.right = node.right
                node.right.left = node.left
                node.left = None
                node.right = self.llist.head
                self.llist.head.left = node
                self.llist.head = node
                node.v = value

    def get(self, key):
        if key in self.hmap:
            node = self.hmap[key]
            if node == self.llist.head:
                return node.v
            elif node == self.llist.tail:
                node.left.right = None
                self.llist.tail = node.left
                node.left = None
                node.right = self.llist.head
                self.llist.head.left = node
                self.llist.head = node
                return node.v
            else:
                node.left.right = node.right
                node.right.left = node.left
                node.left = None
                node.right = self.llist.head
                self.llist.head.left = node
                self.llist.head = node
                return node.v
        return "key not in cache"

def main():
    cache = Cache(5)
    cache.add('oi', 2)
    cache.add('lucas', 5)
    cache.add('pedro',42)
    cache.add('narcelio', 7)
    cache.add('ime', 9)
    print(cache.llist)
    cache.add('marcelo',43)
    print(cache.llist)
    cache.add('lucas', 5)
    print(cache.llist)
    cache.add('narcelio',9)
    print(cache.llist)
    print(cache.get('lucas'))
    print(cache.get('lucas'))
    print(cache.get('narcelio'))
    print(cache.get('pedro'))
    print(cache.get('ragatanga'))
    print(cache.llist)

main()
