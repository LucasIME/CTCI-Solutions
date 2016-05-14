def merge(A, B):
    curA = len(A) - len(B) -1 
    curB = len(B) -1
    curTot = len(A) -1
    while curB >=0:
        if curA >=0 and A[curA] > B[curB]:
            A[curTot] , A[curA] = A[curA] , A[curTot]
            curA -= 1
        else:
            A[curTot] = B[curB]
            curB -=1

        curTot -=1

def main():
    A = [1,3,5,7,8,None, None, None]
    B = [0,4,10]
    merge(A,B)
    print A

if __name__ == '__main__':
    main()
