class Listy:
    def __init__(self, v):
        self.v = v;
    def elementAt(self, i):
        if i >= len(self.v):
            return -1
        else:
            return self.v[i];
    def __getitem__(self, i):
        return self.v[i]

def binSearch(v, left, right, target):
    while left <= right:
        mid = (left + right)/2
        elemid = v.elementAt(mid)
        if elemid > target or elemid == -1:
            right = mid-1
        elif elemid < target:
            left = mid+1
        else:
            return mid
    return -1
def findInListy(listy, target):
    tryMax = 1
    while listy.elementAt(tryMax) != -1 and listy.elementAt(tryMax) < target:
        tryMax <<= 1
    return binSearch(listy,tryMax/2, tryMax, target)

def main():
    v = Listy([1,4,5,10,14,19,20])
    print findInListy(v, 14)
if __name__ == "__main__":
    main()
