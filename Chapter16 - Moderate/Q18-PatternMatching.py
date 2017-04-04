import math

def match(pattern, value):
    mainChar = pattern[0]
    altChar = 'b' if mainChar == 'a' else 'a'
    mainFreq = 0
    altFreq = 0
    firstAltIndex = -1
    for i, letter in enumerate(pattern):
        if letter == mainChar:
            mainFreq +=1
        else:
            altFreq += 1
            if firstAltIndex == -1:
                firstAltIndex = i

    for i in range(len(value)+1):
        main = value[:i]
        mainLen = len(main)
        realAltIndex = firstAltIndex*mainLen 
        altLen = 0 if altFreq == 0 else (len(value) - mainLen*mainFreq) // altFreq
        alt = value[realAltIndex: realAltIndex + altLen]
        
        tempResp = ""
        for letter in pattern:
            if letter == mainChar:
                tempResp += main
            else:
                tempResp += alt
        if tempResp == value:
            return True
    return False


def main():
    pattern = "aabab"
    value = "catcatgocatgo"
    print(match(pattern, value))
    print(match("a", value))
    print(match("b", value))
    print(match("ab", value))
    print(match("aabb", value))


main()