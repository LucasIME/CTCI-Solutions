def isPermutation(s1, s2):
    d1 = {}
    d2 = {}
    for letter in s1:
        if letter not in d1:
            d1[letter] = 1
        else:
            d1[letter] +=1
    for letter in s2:
        if letter not in d2:
            d2[letter] = 1
        else:
            d2[letter] +=1
    if d1 != d2:
        return False
    return True

def main():
    s1 = "rola"
    s2 = "orla"
    print isPermutation(s1, s2)

main()
