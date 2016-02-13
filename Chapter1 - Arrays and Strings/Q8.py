def f(m):
    rows = [i for i in range(len(m))]
    columns = [i for i in range(len(m))]
    n = len(m) -1
    i = 0
    while i < len(rows):
        for j in range(len(columns)):
            if m[rows[i]][columns[j]] == 0:
                mark(m, rows[i], columns[j])
                del rows[i]
                del columns[j]
                break
        i+=1
    return m

def mark(m,i, j):
    for n in range(len(m)):
        m[n][j] = 0
    for n in range(len(m[i])):
        m[i][n] = 0

def main():
    m = [ [1,0,3], [4,5,6], [7,8,0], [3,9,10] ]
    for line in m:
        print line
    print ''
    m = f(m)
    for line in m:
        print line

if __name__ == '__main__':
    main()
