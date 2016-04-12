def count1(n):
    count = 0
    while n > 0:
        n = n & (n-1)
        count+=1
    return count

def conversion(a,b):
    diffBits = a ^ b
    return count1(diffBits)

def main():
    a = 29
    b = 15
    print conversion(a,b)
if __name__ == '__main__':
    main()
