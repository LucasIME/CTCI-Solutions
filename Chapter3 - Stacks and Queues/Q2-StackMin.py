class customStack():
    def __init__(self):
        self.stack = []
        self.minStack = []
    def add(self, item):
        self.stack.append(item)
        if len(self.minStack) ==  0 or  item <= self.minStack[-1]:
            self.minStack.append(item)
    def pop(self):
        value = self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
    def getMin(self):
        return self.minStack[-1]
def main():
    s = customStack()
    s.add(10)
    print s.getMin()
    s.add(15)
    print s.getMin()
    s.add(8)
    print s.getMin()
    s.pop()
    print s.getMin()


if __name__ == '__main__':
    main()
