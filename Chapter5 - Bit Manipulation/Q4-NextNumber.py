def count1(n):
    count = 0
    while n > 0:
        count += n&1
        n >>= 1
    return count

def nextLargest(n):
    mycount = count1(n)
    cur = n+1
    while True:
        if count1(cur) == mycount:
            return cur
        cur +=1

def nextSmallest(n):
    mycount = count1(n)
    cur =  n-1
    while True:
        if count1(cur) == mycount:
            return cur
        cur -= 1
def get0after1(n):
    i = 1
    c = 0
    one = False
    while True:
        bit = n&1
        if bit == 1:
            one = True
            c += 1
        if one == True:
            if bit == 0:
                return (i, c)
        i +=1
        n >>=1
def get1after0(n):
    i=1
    c = 0
    zero = False
    while True:
        bit = n&1
        if bit == 0:
            zero = True
        else:
            c += 1
        if zero == True:
            if bit == 1:
                return (i,c-1)
        i += 1
        n >>= 1

def flip(n, i):
    mask = 1 << (i-1)
    n = n ^ mask
    return n

def fastNext(n):
    i, c = get0after1(n)
    n = flip(n, i)
    n = n & ( (~0) << i-1)
    n = n | ( (1 << (c-1)) -1 )
    return n
def fastSmallest(n):
    i, c = get1after0(n)
    n = flip(n, i)
    n = n & ( (~0) << i-1)
    n = n | ( ((1 << (c+1)) -1) << (i - c -2) )
    return n

def main():
    n = 13948
    #n = 10115
    print nextLargest(n)
    print fastNext(n)
    print nextSmallest(n)
    print fastSmallest(n)

if __name__ == '__main__':
    main()
