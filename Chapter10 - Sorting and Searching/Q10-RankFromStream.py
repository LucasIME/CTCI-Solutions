
class RankNode():
    def __init__(self, data):
        self.left_size = 0
        self.left = None
        self.right = None
        self.data = data

    def insert(self, number):
        if number <= self.data:
            if self.left != None:
                self.left.insert(number)
            else:
                self.left = RankNode(number)
            self.left_size+=1
        else:
            if self.right != None:
                self.right.insert(number)
            else:
                self.right = RankNode(number)
    def getRank(self, number):
        if number == self.data:
            return self.left_size
        elif number < self.data:
            if self.left == None:
                return -1
            else:
                return self.left.getRank(number)
        else:
            right_rank =  -1 if self.right == None else self.right.getRank(number)
            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank
            k
class dataStructure():
    def __init__(self):
        self.root  = None

    def track(self, number):
        if self.root == None:
            self.root = RankNode(number)
        else:
            self.root.insert(number)

    def getRankOfNumber(self, number):
        return self.root.getRank(number)

def main():
    ds = dataStructure()
    v = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    for num in v:
        ds.track(num)
    print ds.getRankOfNumber(1)
    print ds.getRankOfNumber(3)
    print ds.getRankOfNumber(4)

if __name__ == '__main__':
    main()
