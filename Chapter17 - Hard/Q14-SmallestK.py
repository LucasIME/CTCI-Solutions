import heapq

def k_smallest(array, k):
    if k < 0 or k > len(array):
        return None
    if k == len(array):
        return array

    heap = []
    for item in array:
        if len(heap) < k:
            heapq.heappush(heap, -item)
        else:
            if -item > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -item)

    return [-x for x in heap]

def main():
    array = [5, 1, 2, 10, 15, 23, 7, 3, 3, 7]
    k = 4
    print(k_smallest(array, k))
    print(k_smallest(array, 6))
    print(k_smallest(array, 8))

main()
