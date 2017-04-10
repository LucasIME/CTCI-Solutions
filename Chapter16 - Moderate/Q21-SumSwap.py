def sumSwap(v1, v2):
    sa = sum(v1)
    sb = sum(v2)
    map2 = { x:True for x in v2}
    for a in v1:
        b = a - (sa - sb)/2
        if b in map2:
            return (a,b)
    return None
def main():
    v1 = [4, 1, 2, 1, 1, 2]
    v2 = [3, 6, 3, 3]
    print(sumSwap(v1, v2))
    v1 = [3, 4, 1, 2, 1]
    v2 = [1, 2, 4]
    print(sumSwap(v1, v2))
    v1 = [3, 4, 1, 2, 1]
    v2 = [1, 3, 4]
    print(sumSwap(v1, v2))
main()

