from collections import defaultdict

def contiguousSequence(v):
    maxNow = 0
    maxTot = 0
    for item in v:
        maxNow = max(maxNow+item, item)
        maxTot = max(maxTot, maxNow)
    return maxTot

def main():
    v = [2, -8, 3, -2, 4, -10]
    print(contiguousSequence(v))

main()