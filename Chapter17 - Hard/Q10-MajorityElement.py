def majority(l):
    candidate = getCandidate(l)
    return candidate if validate(candidate, l) else -1

def getCandidate(l):
    major = None
    freq = 0
    for letter in l:
        if freq == 0:
            major = letter
        if letter == major:
            freq += 1
        else:
            freq -= 1
    return major

def validate(major, l):
    count = 0
    for letter in l:
        if letter == major:
            count += 1
    return count > len(l)/2

def main():
    l = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    print(majority(l))
    print(majority([1,3,9,3,9]))
    print(majority([4,4,4,4,1,2,3]))

main()