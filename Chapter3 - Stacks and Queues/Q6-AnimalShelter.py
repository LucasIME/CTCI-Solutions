class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def appendToEnd(self, data):
        current = self
        while current.next != None:
            current = current.next
        current.next = Node(data)
    def __repr__(self):
        resp = ""
        current = self
        while current.next != None:
            resp += current.data.__repr__() + "->"
            current = current.next
        resp += current.data.__repr__()
        return resp
    def size(self):
        n = 0
        current = self
        while current.next != None:
            n+=1
            current = current.next
        return n
    def peek(self):
        current = self
        while current.next != None:
            current = current.next
        return current.data
    def pop(self):
        current = self
        while current.next != None and current.next.next != None:
            current = current.next
        current.next = current.next.next
class Animal():
    def __init__(self, name):
        self.name = name
        self.order = 0
    def setOrder(self, order):
        self.order = order
    def getOrder(self):
        return self.order
    def isOlderThan(self, otherAnimal):
        return self.order > otherAnimal.getOrder()
    def __repr__(self):
        return self.name +  " : " + str(self.order)
class Cat(Animal):
    def __init__(self, data):
        Animal.__init__(self,data)

class Dog(Animal):
    def __init__(self, data):
        Animal.__init__(self, data)

class AnimalShelter():
    def __init__(self):
        self.dogs = Node(Dog('dog'))
        self.cats = Node(Cat('cat'))
        self.order = 0
    def enqueue(self, animal):
        animal.setOrder(self.order)
        self.order+=1
        if isinstance(animal, Dog):
            self.dogs.appendToEnd(animal)
        elif isinstance(animal, Cat):
            self.cats.appendToEnd(animal)
    def dequeueAny(self):
        if self.dogs.size() == 0:
            return self.dequeueCat()
        elif self.cats.size() ==0:
            return self.dequeueDog()
        dog = self.dogs.peek()
        cat = self.cats.peek()
        if dog.isOlderThan(cat):
            return self.dequeueDog()
        else:
            return self.dequeueCat()
    def dequeueDog(self):
        dog = self.dogs.peek()
        self.dogs.pop()
        return dog
    def dequeueCat(self):
        cat = self.cats.peek()
        self.cats.pop()
        return cat

def main():
    s = AnimalShelter()
    s.enqueue(Cat('Benny'))
    s.enqueue(Cat('Jerry'))
    s.enqueue(Dog('Bob'))
    s.enqueue(Cat('Benny2'))
    s.enqueue(Dog('pluto'))
    s.enqueue(Dog('Peito'))
    s.enqueue(Dog('Rafa'))
    s.enqueue(Dog('Bunda'))
    s.enqueue(Cat('Jets'))
    print s.dogs
    print s.cats
    print s.dequeueAny()
    print s.dequeueCat()
    print s.dequeueDog()
if __name__ == '__main__':
    main()
