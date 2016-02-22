class SetOfStacks():
    def __init__(self, n):
        self.stacks = [ [] ]
        self.capacity = n
    def push(self, item):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(item)
    def pop(self):
        if len(self.stacks[-1]) == 0:
            del self.stacks[-1]
        self.stacks[-1].pop()
    def popAt(self, index):
        self.stacks[index].pop()
    def __repr__(self):
        return str(self.stacks)
def main():
    s = SetOfStacks(2)
    s.push(10)
    s.push(15)
    s.push(8)
    s.push(8)
    s.push(8)
    s.push(8)
    s.push(8)
    s.push(8)
    s.push(8)
    s.push(8)
    s.push(8)
    print s
    s.pop()
    print s
    s.pop()
    print s
if __name__ == '__main__':
    main()
