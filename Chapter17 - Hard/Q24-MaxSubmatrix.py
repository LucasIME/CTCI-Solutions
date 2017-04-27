def maxSubmatrix(matrix):
    sumMatrix = [[x for x in row] for row in matrix]
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if col == 0 and row == 0:
                continue
            elif row == 0:
                sumMatrix[row][col] +=  sumMatrix[row][col-1]
            elif col == 0:
                sumMatrix[row][col] += sumMatrix[row-1][col]
            else:
                sumMatrix[row][col] += sumMatrix[row-1][col] + sumMatrix[row][col-1] - sumMatrix[row-1][col-1]

    maxTot = 0
    for row in range(0, len(matrix)):
        for row2 in range(row+1, len(matrix)):
            maxSof = 0
            for col in range(0, len(matrix[row])):
                curSubMatrix = getColSum(sumMatrix, row, row2, col)
                maxSof = max(maxSof + curSubMatrix, curSubMatrix)
                maxTot = max(maxSof, maxTot)
    
    return maxTot

def getSubMatrixSum(sumMatrix, rowTop, colTop, rowBot, colBot):
    if rowTop == 0 and colTop == 0:
        return sumMatrix[rowBot][colBot] 
    elif rowTop == 0:
        return sumMatrix[rowBot][colBot] - sumMatrix[rowBot][colTop-1]
    elif colTop == 0:
        return sumMatrix[rowBot][colBot] - sumMatrix[rowTop-1][colBot]
    return sumMatrix[rowBot][colBot] - sumMatrix[rowBot][colTop-1] - sumMatrix[rowTop-1][colBot] + sumMatrix[rowTop-1][colTop-1]

def getColSum(sumMatrix, rowTop, rowBot, col):
    if rowTop == 0 and col == 0:
        return sumMatrix[rowBot][col] 
    elif rowTop == 0:
        return sumMatrix[rowBot][col] - sumMatrix[rowBot][col-1]
    elif col == 0:
        return sumMatrix[rowBot][col] - sumMatrix[rowTop-1][col]
    return sumMatrix[rowBot][col] - sumMatrix[rowBot][col-1] - sumMatrix[rowTop-1][col] + sumMatrix[rowTop-1][col-1]

def main():
    matrix = [[-1, 5, 2], [1, -3, 9], [10, -7, 6]]
    print(maxSubmatrix(matrix))
    matrix2 = [[-2, 55, 40], [22, 77, -30], [13, -44, -100]]
    print(maxSubmatrix(matrix2))
    matrix3 = [[1, 2, 3], [3, 2, 1]]
    print(maxSubmatrix(matrix3))

main()