def getPath(maze):
    newMaze = maze
    for i in range(len(newMaze)):
        for j in range(len(newMaze[i])):
            if newMaze[i][j] == 0:
                newMaze[i][j] = []
    print "New Maze:"
    print newMaze

    for i in range(1,len(newMaze)):
        if newMaze[i-1][0] != 'x':
            newMaze[i][0] = newMaze[i-1][0] + ['down']
    for i in range(1, len(newMaze[0])):
        if newMaze[0][i] != 'x':
            newMaze[0][i] = newMaze[0][i-1] + ['right']
    for i in range(1, len(newMaze)):
        for j in range(1, len(newMaze[i])):
            if newMaze[i][j] != 'x':
                if newMaze[i-1][j] != 'x':
                    newMaze[i][j] = newMaze[i-1][j] + ['down']
                elif newMaze[i][j-1] != 'x':
                    newMaze[i][j] = newMaze[i][j-1] + [ 'right']
    print "New New Maze:"
    print newMaze
    return newMaze[len(newMaze)-1][len(newMaze[len(newMaze)-1])-1]

def main():
    maze = [ [0 for i in range(5)] for j in range(6)]
    maze[1][1] = 'x'
    maze[3][4] = 'x'
    for line in maze:
        print line
    resp = getPath(maze)
    print "Path:"
    print resp
if __name__ == '__main__':
    main()
