def editDistance(w1, w2):
    if len(w1) != len(w2):
        return False
    distance = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            distance += 1
    return distance

def wordTransformer(w1, w2, dictionary):
    visited = set()
    q = [(w1, [])]
    while q:
        current, path = q.pop()
        if current == w2:
            return path + [w2]
        if current not in visited:
            visited.add(current)
            for word in dictionary:
                if editDistance(current, word) == 1:
                    q.insert(0, (word, path + [current]))


def main():
    w1 = "DAMP"
    w2 = "LIKE"
    d = {'DAMP', 'LIKE', 'LAMP', 'LIMP', 'LIKE', 'LIME', 'AGOSTO', 'VILLAS', 'LOL'}
    print(wordTransformer(w1, w2, d))

main()