import random
import heapq
import statistics

class Handler:
    def __init__(self):
        self.median = None
        self.minheap = []
        self.maxheap = []

    def handle(self, num):
        if num >= self.getMedian():
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        self.updateHeap()

    def getMedian(self):
        minTop = self.minheap[0] if len(self.minheap) > 0 else 0
        maxTop = -self.maxheap[0] if len(self.maxheap) > 0 else 0

        if len(self.minheap) != len(self.maxheap):
            return minTop
        return (minTop + maxTop)/2

    def updateHeap(self):
        if len(self.minheap) - len(self.maxheap) > 1:
            top = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -top)
        elif len(self.minheap) < len(self.maxheap):
            top = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, top)

def main():
    handler = Handler()
    v = [random.randint(0, 20000) for i in range(2000)]
    print(v)
    for i, n in enumerate(v):
        handler.handle(n)
        print(handler.getMedian())
        if handler.getMedian() != statistics.median(v[:i+1]):
            print("YOU GOT IT WRONG MOTHERFUCKER")
            return
            
main()