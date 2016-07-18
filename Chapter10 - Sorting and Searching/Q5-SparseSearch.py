
def binSearch(v, left, right, target):
    mid = (left + right)/2
    if target == v[mid]:
        return mid
    if right < left:
        return -1
    if v[mid] == "":
        ret1 = binSearch(v, left, mid-1, target)
        if ret1 != -1:
            return ret1
        else:
            return binSearch(v, mid+1, right, target)
    else:
        if target > v[mid]:
            return binSearch(v, mid+1, right, target)
        else:
            return binSearch(v, left, mid-1, target)

def main():
    v = ["at", "", "", "", "ball", "",  "", "car", "", "", "dad", "", ""];
    print binSearch(v,0, len(v)-1, "ball")
if __name__ == "__main__":
    main()
