def hanoi(n):
    realhanoi(n, 1, 3, 2)

def realhanoi(n, origin, destination, buff):
    if n==0:
        return
    realhanoi(n-1, origin, buff, destination)
    print str(origin) + "->" + str(destination)
    realhanoi(n-1, buff, destination, origin)

def main():
    n = 10
    hanoi(n)
if __name__ == '__main__':
    main()
