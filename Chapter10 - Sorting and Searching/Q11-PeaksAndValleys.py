def sortIntoPeaks(v):
    for i in range(1, len(v), 2):
        biggestIndex = maxIndex(v, i-1, i, i+1)
        if i!= biggestIndex:
            swapIndex(v, i, biggestIndex)
    return v
def maxIndex(v, a, b, c):
    aValue = v[a] if a >=0 and a< len(v) else float('-inf')
    bValue = v[b] if b >=0 and b< len(v) else float('-inf')
    cValue = v[c] if c >=0 and c< len(v) else float('-inf')

    maxi = max(aValue, bValue, cValue)

    if aValue == maxi:
        return a
    elif bValue == maxi:
        return b
    else:
        return c

def swapIndex(v, i1, i2):
    v[i1], v[i2] = v[i2] ,v[i1]

def main():
    v = [5, 3, 1, 2, 3]
    print sortIntoPeaks(v)
    v2 = [0, 1, 4, 7, 8, 9]
    print sortIntoPeaks(v2)
if __name__ == '__main__':
    main()
