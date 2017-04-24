def count2Range(n):
    count = 0
    length = len(str(n))
    for digit in range(length):
        count += count2RangeAtDigit(n, digit)
    return count

def count2RangeAtDigit(n, d):
    pow10 = 10 ** d
    nextPow10 = pow10 * 10
    right = n % pow10

    roundDown = n - n % nextPow10
    roundUp = roundDown + nextPow10

    digit = (n // pow10) % 10

    if digit < 2:
        return roundDown // 10
    elif digit == 2:
        return roundDown // 10 + right + 1
    else:
        return roundUp // 10

def main():
    print(count2Range(25))
    print(count2Range(97))
    print(count2Range(100))
    print(count2Range(102))
    print(count2Range(200))

main()