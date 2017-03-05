from collections import defaultdict

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

def bestLine(pointList):
    maxi = 0
    resp = None
    d = defaultdict(int)
    for i, point in enumerate(pointList):
        for j in range(i+1, len(pointList)):
            point2 = pointList[j]
            line = getLineFromPoints(point, point2)
            linepair = (line.m, line.c)
            d[linepair] +=1
            if d[linepair] > maxi:
                maxi = d[linepair]
                resp = linepair
    return resp
    
def main():
    pointList = [(0,0), (1,1), (3,5), (-2,-2), (9,9), (6,7), (-1,3)]
    print(bestLine(pointList))

main()