def livingPeople(l):
    v = [0 for x in range(102)]
    for pair in l:
        v[pair[0] - 1900]+=1
        v[pair[1] + 1 - 1900]-=1
    maxi = 0
    cur = 0
    year = 1900
    for i in range(len(v)):
        item = v[i]
        cur += item
        if cur >= maxi:
            maxi = cur
            year = 1900 + i
        maxi = max(maxi, cur)
    return year
    
def main():
    l = [ (1900, 1950), (1900, 1950), (1920, 1930), (1900, 2000), (1947, 1980), (1920, 1950) ]
    print(livingPeople(l))

main()