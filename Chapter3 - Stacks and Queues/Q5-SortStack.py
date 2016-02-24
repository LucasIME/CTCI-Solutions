def sortStack(stack):
    sortedStack = []
    while len(stack) > 0:
        curr = stack.pop()
        while len(sortedStack) > 0 and sortedStack[-1] > curr:
            stack.append(sortedStack.pop())
        sortedStack.append(curr)
    return sortedStack

def main():
    s = [ 3, 4, 6, 2, 1, 55, 9, 12, 92, 0]
    s = sortStack(s)
    print s
if __name__ == '__main__':
    main()
