def getSignOf(n):
    return (n >> 31) & 1

def numberMax(n1, n2):
    s1 = getSignOf(n1)
    s2 = getSignOf(n2)
    s3 = getSignOf(n1 - n2)
    k = getSignOf(n1-n2)
    q = k ^ 1
    return n1*q + n2*(1-q)

def main():
    print(numberMax(1,2))
    print(numberMax(-1,5))
    print(numberMax(3,3))
    print(numberMax(0,0))
    print(numberMax(13,0))
    print(numberMax(-5,-2))

main()