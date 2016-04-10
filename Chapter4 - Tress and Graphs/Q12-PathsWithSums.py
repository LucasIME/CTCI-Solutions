from node import *

def getAllPaths(root):
    paths = []
    jafoi = set()
    queue = [(root, [])]
    while len(queue) != 0:
        current = queue.pop()
        if current[0] not in jafoi:
            jafoi.add(current[0])
            #paths.append( current[1] + [current[0].data] )
            if current[0].left != None:
                queue.insert(0, ( current[0].left, current[1] + [ current[0].data] ) )
            if current[0].right != None:
                queue.insert(0, (current[0].right, current[1] + [current[0].data] ) )
            if current[0].left == None and current[0].right == None:
                paths.append( current[1] + [current[0].data] )
    return paths

def getSubsequenceSum(path, targetSum):
    mapData = { 0 : [-1]}
    runningSum = 0
    resp = []
    for i in range(len(path)):
        runningSum += path[i]
        if runningSum - targetSum in mapData:
            for index in mapData[runningSum - targetSum ]:
                resp.append( path[index+1: i+1] )
        if runningSum not in mapData:
            mapData[runningSum] = [i]
        else:
            mapData[runningSum].append(i)
    return resp

def getPathsWithSum( root, num):
    allPaths = getAllPaths(root)
    resp = []
    for path in allPaths:
        tempSeq =  getSubsequenceSum( path, num)
        for subSeq in tempSeq:
            if subSeq != None and subSeq not in resp:
                resp.append(subSeq)
    return resp

def main():
    a = BNode(1)
    a.left = BNode(0)
    a.right = BNode(2)
    a.left.left = BNode(2)
    a.right.left = BNode(1.5)
    a.right.right = BNode(3)
    print getPathsWithSum(a, 3)
    #print getAllPaths(a)
    #print getSubsequenceSum( [1,5,2,3, 4, 8, 7], 7)
if __name__ == '__main__':
    main()
