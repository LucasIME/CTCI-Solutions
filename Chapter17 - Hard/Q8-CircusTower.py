import copy

def circusTower(entry):
    entry.sort()

    solutions = []
    bestSequence = None

    for i, pair in enumerate(entry):
        longestAtIndex = bestSeqAtIndex(entry, solutions, i)
        solutions.insert(i, longestAtIndex)
        bestSequence = max(bestSequence, longestAtIndex)

    return bestSequence

def bestSeqAtIndex(array, solutions, index):
    value = array[index]
    bestSequence = []

    for i in range(index):
        solution = solutions[i]
        if canAppend(solution, value):
            bestSequence = max(solution, bestSequence)

    best = copy.deepcopy(bestSequence)
    best.append(value)

    return best

def canAppend(solution, value):
    if solution is None:
        return False
    if not solution:
        return True

    last = solution[-1]
    return last[0] <= value[0] and last[1] <= value[1]

def main():
    entry = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    print(circusTower(entry))

main()