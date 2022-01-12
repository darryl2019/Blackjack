from random import randint

def initDeck():
    deck = []
    # Add hearts into deck
    for i in range(1, 14):
        deck.append("H" + str(i))
    # Add spades into deck
    for j in range(1, 14):
        deck.append("S" + str(j))
    # Add clubs into deck
    for k in range(1, 14):
        deck.append("C" + str(k))
    # Add diamonds into deck
    for l in range(1, 14):
        deck.append("D" + str(l))
    return deck

def shufDeck(ListArgs):
    shuffledDeck = []
    while(len(ListArgs)!=0):
        value = randint(0, len(ListArgs) - 1)
        shuffledDeck.append(ListArgs[value])
        ListArgs.remove(ListArgs[value])
    return shuffledDeck
