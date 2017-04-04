from collections import defaultdict

def getHits(solution, guess):
    hits = 0
    pseudohits = 0
    frequency = defaultdict(int)
    index = [0 for i in range(len(solution))]
    
    for i, letter in enumerate(guess):
        if letter == solution[i]:
            hits+=1
        else:
            frequency[solution[i]] += 1

    for i, letter in enumerate(guess):
        if guess[i] != solution[i] and frequency[letter] > 0:
            pseudohits+=1
            frequency[letter]-=1

    return [hits, pseudohits]

def main():
    solution = "RGBY"
    guess = "GGRR"
    print(getHits(solution, guess))
    print(getHits("RGGB", "YRGB"))

main()