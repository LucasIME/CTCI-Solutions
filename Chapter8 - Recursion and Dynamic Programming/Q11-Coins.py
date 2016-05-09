def coins(n):
    coinSet = [25, 10, 5, 1]
    m = [  [0 for i in range(len(coinSet))] for j in range(n+1)]
    return makeChange( n, coinSet, 0, m)

def makeChange(n, coinSet, index, m):
    if m[n][index] > 0:
        return m[n][index]
    if index >= len(coinSet) -1:
        return 1
    denomAmount = coinSet[index]
    ways = 0
    i = 0
    while i*denomAmount <= n:
        amountRemaining = n - i*denomAmount
        ways += makeChange(amountRemaining, coinSet, index+1, m)
        i+=1
    m[n][index] = ways
    return ways

def main():
    n = 6
    print coins(n)
if __name__ == '__main__':
    main()
