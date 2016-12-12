def f(wordArray, word):
    dic = makeDict(wordArray)
    if word not in dic:
        return 0
    else:
        return dic[word]

def makeDict(wordArray):
    d = {}
    for word in wordArray:
        if word not in d:
            d[word] = 1
        else:
            d[word]+=1
    return d

def main():
    bookText = "The book is on the Table. Did you hear me? The book is on the motherfucking table, my friend."
    book = bookText.split(" ")
    print(f(book, "the"))
    print(f(book, "naga"))

main()