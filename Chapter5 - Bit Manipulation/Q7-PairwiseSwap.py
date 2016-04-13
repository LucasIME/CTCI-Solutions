def createMask(n):
   # init = 1
    #while init < n:
    #    init <<= 2
    #    init +=1
    #return init
    return 0x55555555

def pairwiseSwap(n):
    mask = createMask(n)
    n2 = n
    n = n & mask
    n <<= 1
    n2 = n2 >> 1
    n2 = n2 & mask
    return n | n2

def main():
    n = 1329
    print n, bin(n)
    print pairwiseSwap(n), bin(pairwiseSwap(n))
if __name__ == '__main__':
    main()
