def findKthWithFactors(k, factors=[3,5,7]):
    if k < 0:
        return 0

    val = 0
    q3 = [1]
    q5 = []
    q7 = []

    for i in range(k):
        v3 = q3[0] if q3 else float('inf')
        v5 = q5[0] if q5 else float('inf')
        v7 = q7[0] if q7 else float('inf')

        val = min(v3, v5, v7)

        if val == v3:
            del q3[0]
            q3.append(3*val)
            q5.append(5*val)
        elif val == v5:
            del q5[0]
            q5.append(5*val)
        elif val == v7:
            del q7[0]
        q7.append(7*val)

    return val

def main():
    for i in range(100):
        print(findKthWithFactors(i))

main()