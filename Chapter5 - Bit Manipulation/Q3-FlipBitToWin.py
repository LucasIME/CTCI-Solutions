def flipToWin(n):
    nonEdit = 0
    edit = 0
    maxi = 0
    while n >0:
        temp = n&1
        if temp == 1:
            nonEdit += 1
            edit+=1
        else:
            edit = nonEdit + 1
            nonEdit = 0
        last = temp
        n >>=1
        maxi = max(maxi, edit, nonEdit)
    return maxi


def main():
    n = 1775
    print flipToWin(n)

if __name__ == '__main__':
    main()
