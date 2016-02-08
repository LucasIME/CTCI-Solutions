def f(s):
    s = s.lower()
    d = {}
    for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] +=1
    numberOfOdd = 0
    for letter, count in d.items():
        if letter!= ' ' and count%2 == 1:
            numberOfOdd+=1
        if numberOfOdd > 1:
            return False
    return True
def main():
    s = "Tact Coa"
    print f(s)

if __name__ == '__main__':
    main()
