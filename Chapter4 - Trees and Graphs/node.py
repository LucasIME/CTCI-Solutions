class Node():
    def __init__(self, data):
        self.data = data
        self.children = []

class Graph():
    def __init__(self, nodes):
        self.nodes = [node for node in nodes]

class Tree():
    def __init__(self, data):
        self.root = Node(data)

class BNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
