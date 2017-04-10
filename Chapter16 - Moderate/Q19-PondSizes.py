def isValid(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        return False
    return True

def water(matrix, row, col):
    if matrix[row][col] != 0:
        return 0
    else:
        matrix[row][col] = -1
        tot = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if isValid(matrix, row+i, col+j):
                    tot += water(matrix, row+i, col + j)
        return tot

def pondSize(matrix):
    resp =  []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                resp.append(water(matrix, row, col))
    return resp

def main():
    matrix = [ [0, 2, 1, 0],
                [0, 1, 0, 1],
                [1, 1, 0, 1],
                [0, 1, 0, 1]]
    print(pondSize(matrix))

main()