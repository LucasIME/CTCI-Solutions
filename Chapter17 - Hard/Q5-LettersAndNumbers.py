def longest(v):
    d = {}
    maxi = 0
    cursum = 0
    subRange = (-1, -1)
    for i, item in enumerate(v):
        if isinstance(item, str):
            cursum +=1
        else:
            cursum -=1
        if cursum in d:
            if i - d[cursum] > maxi:
                maxi = i - d[cursum]
                subRange = (d[cursum], i)
        else:
            d[cursum] = i
    return v[subRange[0]:subRange[1]+1]

def main():
    v = [1, 2, 'a', 'b', 3, 'q', 'q', 'q', 'l ', 'q', 3, 33, 49, 'q', 'q', 'q', 'q', 'q', 9, 0]
    print(longest(v))

main()