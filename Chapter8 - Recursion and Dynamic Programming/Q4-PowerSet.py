from copy import copy

def powerSet(s):
    if len(s) == 0:
        return [ [] ]
    cur = s[0]
    miniSet = powerSet(s[1:])
    extendedSet = []
    for littleSet in miniSet:
        temp = copy(littleSet)
        temp.append(cur)
        extendedSet.append(temp)
    return miniSet + extendedSet


def main():
    s = [5,1,2,9,3]
    print powerSet(s)
if __name__ == '__main__':
    main()
