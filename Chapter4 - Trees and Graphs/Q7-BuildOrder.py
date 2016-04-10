from node import *

def getBuildOrder( projects, dependencies):
    response = []
    outEdges = { project : [] for project in projects}
    inEdges = { project: [] for project in projects}
    for p1, p2 in dependencies:
        outEdges[p2].append(p1)
        inEdges[p1].append(p2)
    while True:
        changed = False
        nodesToRemove = []
        for node in inEdges:
            if inEdges[node] == []:
                changed = True
                response.append(node)
                nodesToRemove.append(node)
                for nextnode in outEdges[node]:
                    inEdges[nextnode].remove(node)
                #del inEdges[node]
        for node in nodesToRemove:
            del inEdges[node]
        if changed == False:
            break
    if len(response) != len(projects):
        return []
    else:
        return response
def main():
    projects = [ 'a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [ ('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd') ]
    #adjmatrix = { project: [p for p in projects] for project in projects  }
    projects2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    dependencies2 = [ ('c', 'f'), ('b', 'f'), ('a', 'f'), ('a', 'b'), ('a', 'c'), ('e', 'a'), ('e', 'b'),  ('g', 'd')]

    print getBuildOrder(projects2, dependencies2) 
if __name__ == '__main__':
    main()
