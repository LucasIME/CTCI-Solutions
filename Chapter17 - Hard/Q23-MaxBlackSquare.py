def getMaxBlackSquare(matrix):
    left = [ [col for col in row] for row in matrix]
    up = [ [col for col in row] for row in matrix]

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col] == 0:
                continue
            else:
                left[row][col] = 1 + left[row][col-1]
                up[row][col] = 1 + up[row-1][col]

    resp = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            biggestSquare = getBiggestSquare(matrix, row, col, left, up)
            resp = max(resp, biggestSquare)
    
    return resp

def getBiggestSquare(matrix, row, col, left, up):
    if matrix[row][col] == 0:
        return 0
    dist = min(left[row][col], up[row][col])
    maxSof = 0
    for i in range(dist+1):
        leftCol = col - i
        upRow = row - i
        if up[row][leftCol] >= i and left[upRow][col] >= i:
            maxSof = i+1

    return maxSof



def main():
    matrix = [[0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0]]
    print(getMaxBlackSquare(matrix))
    matrix2 = [[0, 0, 0], [0, 0, 0]]
    print(getMaxBlackSquare(matrix2))
    matrix3 = [[0, 1], [1, 0]]
    print(getMaxBlackSquare(matrix3))
    matrix3 = [[1, 1, 0], [1, 1, 0]]
    print(getMaxBlackSquare(matrix3))

main()