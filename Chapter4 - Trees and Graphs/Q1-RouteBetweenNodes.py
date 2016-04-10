from node import *

def findRouteDoubleStart(graph, s, f):
    q1= []
    q2 = []
    q1.append(s)
    q2.append(f)
    s1 = set()
    s2 = set()
    while len(q1) !=0 or len(q2) != 0:
        if len(q1) > 0:
            c1 = q1.pop()
            if c1 not in s1:
                s1.add(c1)
                for node in c1.children:
                    q1.insert(0, node)
            if c1 in s2:
                return True
        if len(q2) > 0:
            c2 = q2.pop()
            if c2 not in s2:
                s2.add(c2)
                for node in c2.children:
                    q2.insert(0, node)
            if c2 in s1:
                return True
    return False

def findRoute(graph, a, f):
    q = []
    s = set()
    q.append(a)
    while len(q) > 0:
        current = q.pop()
        if current == f:
            return True
        if current not in s:
            s.add(current)
            for node in current.children:
                q.insert(0, node)
    q.append(f)
    while len(q) > 0:
        current = q.pop()
        if current == f:
            return True
        if current not in s:
            s.add(current)
            for node in current.children:
                q.insert(0, node)
    return False

def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    a.children.append(b)
    #b.children.append(c)
    c.children.append(b)
    b.children.append(a)
    G  = Graph( [a,b,c] )
    print findRoute(G, a, c)

if __name__ == '__main__':
    main()
