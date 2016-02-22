class customQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, item):
        self.stack1.append(item)
    def pop(self):
        if len(self.stack2) > 0:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()
    def __repr__(self):
        return str(self.stack1) + '\n' + str(self.stack2)
def main():
    s = customQueue()
    s.push(10)
    s.push(15)
    s.push(8)
    s.push(7)
    s.push(6)
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    s.push(0)
    print s
    s.pop()
    print s
    s.pop()
    print s
if __name__ == '__main__':
    main()
