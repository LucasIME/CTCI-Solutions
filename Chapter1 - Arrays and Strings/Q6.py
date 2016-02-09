def f(s):
    newString = ""
    counter = 0
    lastLetter  = s[0]
    for letter in s:
        if letter == lastLetter:
            counter+=1
        if letter != lastLetter:
            newString+= lastLetter+str(counter)
            lastLetter = letter
            counter = 1
    newString += letter + str(counter)
    if len(newString) < len(s):
        return newString
    else:
        return s

def main():
    s = "aabcccccaaab"
    print f(s)

if __name__ == '__main__':
    main()
