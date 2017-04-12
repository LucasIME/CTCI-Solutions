from random import randint

def randSet(v, k):
    if k == 0:
        return set()
    if k == 1:
        s = set()
        i = randint(0, len(v)-1)
        s.add(v[i])
        return s
    subSet = randSet(v, k-1)
    i = randint(0, len(v)-1)
    while v[i] in subSet:
        i = randint(0, len(v)-1)
    subSet.add(v[i])
    return subSet

def main():
    v = [1, 9, 3, 10, 7, 2, 7, 8, 9, 15, 13, -1, -5, -29, 3, -3, 24, 17]
    for i in range(10):
        print(randSet(v, i))

main()
