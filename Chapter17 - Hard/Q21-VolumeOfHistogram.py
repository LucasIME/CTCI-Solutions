def calcVolume(histogram):
    maxLeft = [0 for x in histogram]
    maxRight = [0 for x in histogram]

    maxLeftSoFar = 0
    for i, height in enumerate(histogram):
        maxLeft[i] = maxLeftSoFar
        maxLeftSoFar = max(maxLeftSoFar, height)

    maxRightSoFar = 0
    for i in range(len(histogram)-1, -1, -1):
        height = histogram[i]
        maxRight[i] = maxRightSoFar
        maxRightSoFar = max(maxRightSoFar, height)

    volume = 0
    for i, height in enumerate(histogram):
        top = min(maxLeft[i], maxRight[i])
        if top > height:
            volume += top - height

    return volume

def main():
    h = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
    print(calcVolume(h))

main()