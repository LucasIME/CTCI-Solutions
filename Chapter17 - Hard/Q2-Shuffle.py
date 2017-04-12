from random import randint

def shuffleDeck(deck):
    return shuffleHelper(deck, len(deck)-1)

def shuffleHelper(deck, i):
    if i == 0:
        return deck
    shuffleHelper(deck, i-1)
    k = randint(0, i)

    deck[i], deck[k] = deck[k], deck[i]

    return deck 

def shuffleIterative(deck):
    for i in range(len(deck)):
        k = randint(0, i)
        deck[i], deck[k] = deck[k], deck[i]
    return deck

def main():
    cardDeck = [1, 9, 3, 10, 7, 2, 7, 8, 9]
    for i in range(10):
        print(shuffleDeck(cardDeck))
        print(shuffleIterative(cardDeck))

main()
