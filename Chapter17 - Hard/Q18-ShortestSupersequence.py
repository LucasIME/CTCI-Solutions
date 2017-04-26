import heapq

def shortestSupersequence(smallArray,bigArray):
    ht = {x : [] for x in smallArray}
    totalHeap = []

    for i, letter in enumerate(bigArray):
        if letter in ht:
            heapq.heappush(ht[letter], i)
            heapq.heappush(totalHeap, (i, letter))

    mini = totalHeap[0][0]
    maxi = 0
    for x in ht:
        maxi = max(maxi, ht[x][0])

    realMini = mini
    realMax = maxi

    print(mini)
    while totalHeap:
        oldtop = heapq.heappop(totalHeap)
        if len(ht[oldtop[1]]) > 1:
            oldIndex = heapq.heappop(ht[oldtop[1]])
            maxi = max(maxi, ht[oldtop[1]][0])
            if oldIndex == mini:
                if totalHeap:
                    newTop = totalHeap[0]
                    mini = newTop[0]
        print(totalHeap, mini, maxi, realMini, realMax)
        if maxi - mini < realMax - realMini:
            realMini = mini
            realMax = maxi
    return bigArray[realMini:realMax+1]


def main():
    smallArray = [1, 5, 9]
    bigArray = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    print(shortestSupersequence(smallArray, bigArray))

main()