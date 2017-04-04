from collections import defaultdict

def subSort(v):
    left = 0
    right = 0

    maxSoFar = float('-inf')
    for i in range(len(v)):
        if v[i] < maxSoFar:
            right = i
        maxSoFar = max(maxSoFar, v[i])
    
    minSoFar = float('inf')
    for i in range(len(v)-1, -1 ,-1):
        if v[i] > minSoFar:
            left = i
        minSoFar = min(minSoFar, v[i])

    return (left, right)

def main():
    v = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(subSort(v))
    v2 = [1, 2, 3, 7, 10, 2, 10, 11, 5, 21]
    print(subSort(v2))
    v3 = [1, 2, 3, 0]
    print(subSort(v3))
        
main()