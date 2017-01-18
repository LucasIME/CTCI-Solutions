def generateDivingBoard(shorter, longer, k):
    v = set()
    for i in range(k+1):
        v.add( i*shorter + (k-i)*longer)
    return v
        
def main():
    shorter = 3
    longer = 5
    k = 8
    print(generateDivingBoard(shorter, longer, k))

main()