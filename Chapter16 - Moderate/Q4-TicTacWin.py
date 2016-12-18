def checkWin(ticTacGame):
    for line in ticTacGame:
        if line[0] == line[1] and line[1] == line[2]:
            return True
    for col in range(len(ticTacGame)):
        if ticTacGame[0][col] == ticTacGame[1][col] and ticTacGame[1][col] == ticTacGame[2][col]:
            return True
    if ticTacGame[0][0] == ticTacGame[1][1] and ticTacGame[1][1] == ticTacGame[2][2]:
        return True
    if ticTacGame[0][2] == ticTacGame[1][1] and ticTacGame[1][1] == ticTacGame[2][0]:
        return True
    return False

def main():
    print(checkWin([['X', 'X', 'X'],
                    ['X', 'O', 'O'],
                    ['O', 'X', 'O']]))
    print(checkWin([['X', 'O', 'X'],
                    ['O', 'X', 'X'],
                    ['O', 'X', 'O']]))

main()