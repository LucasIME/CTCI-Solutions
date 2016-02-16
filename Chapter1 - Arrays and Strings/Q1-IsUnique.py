def isUnique(s):
    lettersDictionary = {}
    for letter in s:
        if letter not in lettersDictionary:
            lettersDictionary[letter] = True
        else:
            return False
    return True

def isUniqueNoMem(s):
    charList = list(s)
    charList.sort()
    for i in range(1, len(charList)):
        if charList[i] == charList[i-1]:
            return False
    return True

def main():
    s = "TestingString"
    print isUnique(s)    

if __name__ == '__main__':
    main()
