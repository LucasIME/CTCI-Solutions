def smallestDifferences(v1, v2):
    v1.sort()
    v2.sort()
    j = 0
    mini = abs(v1[0] - v2[0])
    pair = ()
    is1Smaller = v1[0] < v2[0]
    for i in range(len(v1)):
        while j < len(v2) and v2[j] < v1[i]:
            j+=1
            mini = abs(v1[i] - v2[j])
        mini = abs(v1[i] - v2[j])
    return mini  

def main():
    v1 = [1, 3, 15, 11, 2]
    v2 = [23, 127, 235, 19, 8]
    print(smallestDifferences(v1,v2))

main()