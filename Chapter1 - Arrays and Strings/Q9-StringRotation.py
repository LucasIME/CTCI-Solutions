def f(s1, s2):
    if len(s2) != len(s1):
        return False
    s1 =  s1 + s1
    if s2 in s1:
        return True
    else:
        return False

def main():
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print f(s1,s2)
if __name__ == '__main__':
    main()
