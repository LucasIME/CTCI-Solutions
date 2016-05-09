def paintFill(screen, i, j , newColor):
    oldColor = screen[i][j]
    smartFill(screen, i, j, newColor, oldColor)

def smartFill(screen, i, j, newColor, oldColor):
    if i <0 or i >= len(screen):
        return
    if j<0 or j >= len(screen[i]):
        return
    if screen[i][j] == oldColor:
        screen[i][j] = newColor
        smartFill(screen, i-1, j, newColor, oldColor)
        smartFill(screen, i, j-1, newColor, oldColor)
        smartFill(screen, i+1, j, newColor, oldColor)
        smartFill(screen, i, j+1, newColor, oldColor)

def main():
    screen = [ [1, 1, 1, 1],
            [1,2, 2, 1],
            [1,2,2,1]]
    print 'Before:'
    for line in screen:
        print line
    paintFill(screen, 1, 1, 3)
    print "After:"
    for line in screen:
        print line
if __name__ == '__main__':
    main()
