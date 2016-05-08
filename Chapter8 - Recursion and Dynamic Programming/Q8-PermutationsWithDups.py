def getPerms(s):
    result = []
    dic = buildFreqTable(s)
    perm(dic, "", len(s), result)
    return result

def buildFreqTable(s):
    resp = {}
    for char in s:
        if char not in resp:
            resp[char] = 1
        else:
            resp[char]+=1
    return resp

def perm(dic, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return

    for char in dic:
        count = dic[char]
        if count > 0:
            dic[char] = count-1
            perm(dic, prefix + char, remaining -1, result)
            dic[char] = count

def main():
    s = "1232"
    print getPerms(s)
if __name__ == '__main__':
    main()
