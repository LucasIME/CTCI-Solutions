from copy import copy

def getPerm(s):
    if len(s) == 0:
        return [ ""]
    if len(s) == 1:
        return [ s ]
    cur = s[0]
    subperm = getPerm(s[1:])
    realSet = []
    for i in range(len(subperm)):
        for j in range(len(subperm[i])+1):
            realSet.append( subperm[i][:j] + cur + subperm[i][j:])
    return realSet

def main():
    s = "123"
    print getPerm(s)
if __name__ == '__main__':
    main()
