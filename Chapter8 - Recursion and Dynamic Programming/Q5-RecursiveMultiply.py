def themultiply(a,b):
    mini, maxi = min(a,b), max(a,b)
    return multiply(a,b)

def multiply(a,b):
    if a==0:
        return 0
    if a==1:
        return b
    else:
        if a%2 == 0:
            return multiply(a/2, b) << 1
        else:
            return (multiply(a/2,b) << 1) + b

def main():
    a ,b = 500, 200
    print themultiply(a,b)

if __name__ == '__main__':
    main()
