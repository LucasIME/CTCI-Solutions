class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def appendToTail(self, data):
        no =  self
        while no.next != None:
            no = no.next
        no.next = Node(data)
    def __repr__(self):
        resp = ""
        no = self
        while no.next != None:
            resp += str(no.data) + ' -> '
            no = no.next
        resp += str(no.data)
        return resp
