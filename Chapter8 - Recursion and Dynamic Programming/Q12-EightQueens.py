GRID_SIZE=8
from copy import copy

def placeQueens(row, columns, results):
    if row == GRID_SIZE:
        results.append(copy(columns))
    else:
        for col in range(GRID_SIZE):
            if checkValid(columns, row, col):
                columns[row] = col
                placeQueens(row+1, columns, results)
def checkValid(columns, row1, column1):
    for row2 in range(row1):
        column2 = columns[row2]
        if column1 == column2:
            return False
        columnDistance = abs(column2 - column1)
        rowDistance = row1-row2
        if columnDistance == rowDistance:
            return False
    return True

def main():
    resp = []
    placeQueens(0, [0 for i in range(GRID_SIZE)], resp)
    for line in resp:
        print line
if __name__ == '__main__':
    main()
