class Square():
    def __init__(self, x1,y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def getCenter(self):
        return ( (self.x2 + self.x1)/2, (self.y2 + self.y1)/2 )

class Line():
    def __init__(self, m, c):
        self.m = m
        self.c = c
    def __repr__(self):
        return "{0}*x + {1}".format(self.m, self.c)

def getLineFromPoints(point1, point2):
    m = 0
    if point1[0] != point2[0]:
        m = (point2[1] - point1[1])/(point2[0] - point1[0])
    c = point1[1] - m * point1[0]
    return Line(m, c)
    

def bisectSquare(square1, square2):
    c1 = square1.getCenter()
    c2 = square2.getCenter()
    if c1 == c2:
        return getLineFromPoints((0,0), c1)
    return getLineFromPoints(c1, c2)
    
def main():
    s1 = Square(1, 1, 5, 5)
    s2 = Square(3,4, 8, 9)
    print(bisectSquare(s1, s2))

main()