class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.m = (point2.y - point1.y) / (point2.x - point1.x)
        self.c = point2.y - self.m * point2.x

def findIntersection(line1, line2):
    if line1.m == line2.m and line1.c != line2.c:
        return "They'll never intersect"
    elif line1.m == line2.m and line1.c == line2.c:
        return "They are the same line"
    else:
        x =  (line2.c - line1.c) / (line1.m - line2.m)
        y = line1.m * x + line1.c
        return Point(x,y)

def main():
    line1 = Line(Point(3, 4), Point(15, 16))
    line2 = Line( Point(3, 6), Point(19, 33))
    point = findIntersection(line1, line2)
    print(point.x, point.y)

main()