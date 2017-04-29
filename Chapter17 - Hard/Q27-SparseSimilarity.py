from collections import defaultdict

def similar_files(files):
    resp = []
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            file1 = files[i]
            file2 = files[j]
            interSize = 0
            for item in file2:
                if item in file1:
                    interSize += 1
            unionSize = len(file1) + len(file2) - interSize
            if interSize > 0:
                similarity = interSize / unionSize
                resp.append((i, j, similarity))
    return resp

def similar_files_optimized(files):
    resp = []
    itemToDoc = defaultdict(list)
    for key, doc in enumerate(files):
        for item in doc:
            itemToDoc[item].append(key)

    pairSim = defaultdict(int)
    for item in itemToDoc:
        if len(itemToDoc[item]) > 1:
            for i in range(len(itemToDoc[item])):
                for j in range(i+1, len(itemToDoc[item])):
                    key1 = itemToDoc[item][i]
                    key2 = itemToDoc[item][j]
                    mini = min(key1, key2)
                    maxi = max(key1, key2)
                    pairSim[(key1, key2)] += 1

    for pair, sim in pairSim.items():
        resp.append((pair[0], pair[1], sim / (len(files[pair[0]]) + len(files[pair[1]]) - sim)))

    return resp



    for i in range(len(files)):
        for j in range(i+1, len(files)):
            file1 = files[i]
            file2 = files[j]
            interSize = 0
            for item in file2:
                if item in file1:
                    interSize += 1
            unionSize = len(file1) + len(file2) - interSize
            if interSize > 0:
                similarity = interSize / unionSize
                resp.append((i, j, similarity))
    return resp

def main():
    f1 = {14, 15, 100, 9, 3}
    f2 = {32, 1, 9, 3, 5}
    f3 = {15, 29, 2, 6, 8, 7}
    f4 = {10, 7}
    f5 = {1, 5, 3}
    f6 = {1, 7, 2, 3}

    files = [f1, f2, f3, f4, f5, f6]
    
    print(similar_files(files))
    print(similar_files_optimized(files))

main()
