def search(matrix, target):
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            col-=1
        else:
            row+=1
    return False

def main():
    matrix = [ [15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
    target = 95
    print search(matrix, target)

if __name__ == '__main__':
    main()
