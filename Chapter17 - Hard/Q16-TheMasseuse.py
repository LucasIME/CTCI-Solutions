def maxMinutes(v):
    oneAway = 0
    twoAway = 0
    for i in range(len(v)-1, -1, -1):
        bestWith = v[i] + twoAway
        bestWithout = oneAway
        current = max(bestWith, bestWithout)
        twoAway = oneAway
        oneAway = current
    return oneAway

def main():
    v = [30, 15, 60, 75, 45, 15, 15, 45]
    print(maxMinutes(v))
    v2 = [75, 105, 120, 75, 90, 135]
    print(maxMinutes(v2))

main()