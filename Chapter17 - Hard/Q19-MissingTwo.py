import math

def oneMissing(v):
    n = len(v) + 1
    expectedSum = (1+n)*n/2
    total = sum(v)
    return expectedSum - total

def twoMissing(v):
    n = len(v) + 2
    expectedSum = (1+n)*n/2
    total = sum(v)

    expectedSquareSum = sum([x*x for x in range(n+1)])
    totalSquared = sum([x*x for x in v])

    normDiff = expectedSum - total # a + b = normDiff
    squaredDiff = expectedSquareSum - totalSquared # a2 + b2 = squaredDiff

    # a2 - a(normDiff) + ((normDiff2 - squaredDiff)/2)
    print(normDiff, squaredDiff)
    pair = solveEquation(1, -normDiff, (normDiff**2 - squaredDiff)/2)

    return pair

def solveEquation(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return (x1, x2)


def main():
    v1 = [1,2,3,5,6,7,8,9]
    print(oneMissing(v1))
    v2 = [1,2,5,6,7,8,9]
    print(twoMissing(v2))
    v3 = [1,3,4,5,6,8,9]
    print(twoMissing(v3))

main()