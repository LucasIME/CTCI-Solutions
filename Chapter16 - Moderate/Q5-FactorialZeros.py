def fatZeros(n):
    zeroCount = 0
    fivePow = 5
    while fivePow <= n:
        zeroCount += n//fivePow
        fivePow *= 5
    return zeroCount

def main():
    print(fatZeros(10))
    print(fatZeros(100))
    print(fatZeros(342))
    print(fatZeros(4234234))

main()