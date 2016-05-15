def newSort(l):
    d = {}
    resp = []
    for word in l:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in d:
            d[sortedWord] = [word]
        else:
            d[sortedWord].append(word)
    for key in d:
        for word in d[key]:
            resp.append(word)
    return resp

def main():
    l = [ 'rola', 'a',  'b', 'alor', 'b', 'ca', 'bbb', 'ac']
    print l
    l = newSort(l)
    print l

if __name__ == '__main__':
    main()
