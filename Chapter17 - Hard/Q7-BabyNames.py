from collections import defaultdict

def merge(names, synonyms):
    graph = getGraph(names)
    connectGraph(graph, synonyms)

    trueFreq = getTrueFreq(graph, names)
    return trueFreq

def getGraph(names):
    graph = defaultdict(list)
    for pair in names:
        name = pair[0]
        graph[name] = []
    return graph

def connectGraph(graph, synonyms):
    for pair in synonyms:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])

def getTrueFreq(graph, names):
    oldFreqs = defaultdict(int)
    for pair in names:
        oldFreqs[pair[0]] = pair[1]
    newFreq = defaultdict(int)

    visited = set()
    queue = []
    for pair in names:
        name = pair[0]
        if name not in visited:
            queue.append(name)
            while queue:
                current = queue.pop()
                visited.add(current)
                newFreq[name] += oldFreqs[current]

                for neighbour in graph[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)
    return newFreq


def main():
    names = [('John', 15), ('Jon', 12), ('Chris', 13), ('Kris', 4), ('Christopher', 19)]
    synonyms = [('Jon', 'John'), ('John', 'Johnny'), ('Chris', 'Kris'), ('Chris', 'Christopher')]
    print(merge(names, synonyms))
    names = [('John', 10), ('Jon', 3), ('David', 2), ('Kari', 3), ('Johnny', 11), ('Carlton', 11), ('Carleton', 2), ('Jonathan', 9), ('Carrie', 5)]
    synonyms = [('Jonathan', 'John'), ('Jon', 'Johnny'), ('Johnny', 'John'), ('Kari', 'Carrie'), ('Carleton', 'Carlton')]
    print(merge(names, synonyms))

main()
