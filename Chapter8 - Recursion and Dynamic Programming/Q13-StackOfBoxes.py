class box():
    def __init__(self, w,h, d):
        self.w = w
        self.h = h
        self.d = d

    def __gt__(self, box2):
        return self.w > box2.w and self.h > box2.h and self.d > box2.d
    def __lt__(self, box2):
        return self.w < box2.w and self.h < box2.h and self.d < box2.d
    def __repr__(self):
        return str( (self.w, self.h, self.d) )

def getMaxHeight(boxArray):
    #boxArray.sort(reverse=True)
    boxArray.sort(cmp=lambda x,y: x.h-y.h, reverse=True)
    print boxArray
    resp = 0
    stackMap = {}
    for i in range(len(boxArray)):
        resp =  max(resp, realMaxHeight(boxArray, i, stackMap))
    print stackMap
    return resp

def realMaxHeight(sortedArray, n, stackMap):
    if n in stackMap:
        return stackMap[n]
    if n== len(sortedArray)-1:
        stackMap[n] = sortedArray[n].h
        return stackMap[n]
    resp = sortedArray[n].h
    for i in range(n+1, len(sortedArray)):
        if sortedArray[n] > sortedArray[i]:
            resp = max( resp, sortedArray[n].h + realMaxHeight(sortedArray, i, stackMap))
    stackMap[n] = resp
    return resp

def main():
    boxArray = [ box(1,2,3), box(4,5,6),box(2,3,1),  box(0,1,2), box(2, 3, 4)]
    print getMaxHeight(boxArray)

if __name__ == '__main__':
    main()
