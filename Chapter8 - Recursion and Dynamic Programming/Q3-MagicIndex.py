
#O(n) and supports repetitions
def findMagic1(v):
    cur = 0
    while cur < len(v):
        if v[cur] == cur:
            return cur
        else:
            cur = max(cur, v[cur]) +1
            #else:
            #    cur+=1
    return None


#logN and does not support repetitions
def findMagic2(v):
    beg = 0
    end =  len(v) -1
    while True:
        cur = (beg + end)/2
        if cur == v[cur]:
            return cur
        elif beg == end:
            return None
        elif cur > v[cur]:
            beg = cur +1
        else:
            end = cur
    return None

#logN and supports repetitions
def findMagic3(v):
    return magicFast(v, 0, len(v)-1)

def magicFast(v, beg, end):
    if end < beg:
        return None

    cur = (end+beg)/2
    if cur == v[cur]:
        return cur

    left = min( cur-1, v[cur])
    leftV = magicFast(v, beg, left)
    if leftV != None:
        return leftV

    right = max(cur+1, v[cur])
    rightV = magicFast(v, right, end)
    return rightV

def main():
    v= [-10, -5, 2,2,2,3,4,7,9,12,13]
    #v = [-1, 0, 1, 3, 4, 9]
    print findMagic1(v)
    print findMagic2(v)
    print findMagic3(v)
if __name__ == '__main__':
    main()
