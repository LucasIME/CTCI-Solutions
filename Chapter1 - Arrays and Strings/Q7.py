def f(m):
    n = len(m) -1
    for i in range( len(m)/2):
        for j in range(i,len(m[i])-1-i):
            temp = m[j][n-i]
            m[j][n-i] = m[i][j]
            m[i][j] = m[n-j][i]
            m[n-j][i] = m[n-i][n-j]
            m[n-i][n-j] = temp
    return m

def main():
    m = [ [1,2,3], [4,5,6], [7,8,9] ]
    m = f(m)
    for line in m:
        print line

if __name__ == '__main__':
    main()
