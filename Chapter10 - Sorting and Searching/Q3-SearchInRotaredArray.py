def find(v, target):
    return findHelper(v, 0, len(v)-1, target)

def findHelper(v, left, right, target):
    mid = (left + right)//2
    if target == v[mid]:
        return mid
    if right < left:
        return -1

    if v[left] < v[mid]:
        if (target >= v[left] and target < v[mid]):
            return findHelper(v, left, mid-1, target)
        else:
            return findHelper(v, mid+1, right, target)
    elif v[mid] < v[left]:
        if target > v[mid] and target <= v[right]:
            return findHelper(v, mid+1, right, target)
        else:
            return findHelper(v, left, mid-1, target)
    elif v[left] ==  v[mid]:
        if v[mid] != v[right]:
            return findHelper(v, mid+1, right, target)
        else:
            result = findHelper(v, left, mid-1, target)
            if result == -1:
                return findHelper(v, mid+1, right, target)
            else:
                return result
    return -1

def main():
    v = [15, 16, 19, 20, 25, 1, 3, 4, 5, 5, 5,  5, 7, 10, 14]
    v2 = [15, 16, 19, 20, 25, 1, 3, 3, 3, 4, 5, 7]
    v3 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 13, 14]
    v4 = [2,2,2,3,4,2]
    index = find(v, 5)
    index1 = find(v2, 5)
    index2 = find(v3, 5)
    index3 = find(v4, 2)
    print index, index1, index2, index3

if __name__ == '__main__':
    main()
