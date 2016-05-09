def getParens(n):
    s = ["" for i in range(2*n)]
    resp = []
    addParen(resp, n, n, s, 0)
    return resp

def addParen( l, leftRem, rightRem, s, count):
    if leftRem < 0 or rightRem < leftRem:
        return
    if leftRem == 0 and rightRem ==0:
        l.append( ''.join(s))
    else:
        if leftRem > 0:
            s[count] = '('
            addParen(l, leftRem-1, rightRem, s, count+1)
        if rightRem > leftRem:
            s[count] = ')'
            addParen(l, leftRem, rightRem-1, s, count+1)
def main():
    n = 4
    print getParens(n)
if __name__ == '__main__':
    main()
