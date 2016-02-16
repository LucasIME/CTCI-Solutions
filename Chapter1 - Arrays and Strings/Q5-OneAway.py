def f(s1, s2):
    #Checks lengths
    if abs(len(s1)-len(s2)) > 1:
        return False
    #Smaller string in s1, longer one in s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i1 = 0
    i2 = 0
    diff = False
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            if diff:
                return False
            diff = True
            if len(s1) == len(s2):
                i1+=1
        else:
            i1+=1
        i2+=1
    return True

def main():
    s1 = "pale"
    s2  = "pble"
    print f(s1, s2)

if __name__ == '__main__':
    main()
