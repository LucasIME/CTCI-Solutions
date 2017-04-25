def findDist(w1, w2, bookWords):
    if w1 not in bookWords or w2 not in bookWords:
        return -1

    l1 = bookWords[w1]
    l2 = bookWords[w2]

    dist = float('inf')
    p1 = 0
    p2 = 0
    while p1 < len(l1) and p2<len(l2):
        dist = min(dist, abs(l1[p1] - l2[p2]))
        if l1[p1] < l2[p2]:
            p1 += 1
        else:
            p2 += 1
    
    return dist


def main():
    bookWords = {'table':[2,200,150,250,333,1337], 'row':[158,248,323]}
    word1 = 'table'
    word2 = 'row'
    print(findDist(word1, word2, bookWords))
    bookWords = {'table':[1, 2, 9, 15, 25], 'row':[4, 10, 19]}
    print(findDist(word1, word2, bookWords))

main()