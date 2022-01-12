from tkinter import *
from initDeck import *
from calcHandValue import *
root = Tk()

label1 = Label(root, text="No of Decks to play with: ")
entry1 = Entry(root)
label1.pack()
entry1.pack()

label2 = Label(root, text="No of Hands to play with: ")
entry2 = Entry(root)
label2.pack()
entry2.pack()

playersFrame = Frame(root)
cardFrame = Frame(root)
dealersFrame = Frame(root)

handScore = []
handsValid = []
handCounter = 0
position = 0


def numberOfDecks():
  numberOfDecksInit = entry1.get()
  return numberOfDecksInit

def numberOfHands():
  numberOfHandsInit = entry2.get()
  return numberOfHandsInit

def dealer(dealersHand,playerAndCards,deck):
  positionOfDealersNextCard = 2
  for y in range(int(numberOfHands())):
    positionOfDealersNextCard = positionOfDealersNextCard + len(playerAndCards[y])

  print(positionOfDealersNextCard, "POS")
  #Dealers sticks on 16 bust on over 21
  while(int(calcValue(dealersHand))<=16):
    print(deck[positionOfDealersNextCard])
    print(deck)
    dealersHand.append(deck[positionOfDealersNextCard])
    dealersNextCardString = 'images/' + deck[positionOfDealersNextCard] + '.png'
    dealersNextCard = PhotoImage(file=dealersNextCardString)
    dealersNextCard = dealersNextCard.subsample(2)
    nextCardLabel = Label(dealersFrame, image=dealersNextCard)
    nextCardLabel.image = dealersNextCard
    nextCardLabel.grid(column=len(dealersHand),row=0)
    positionOfDealersNextCard=positionOfDealersNextCard+1

  for y in range(int(numberOfHands())):
    isBust = False
    isDealerBust = False
    if (int(calcValue(playerAndCards[y]) > 21)):
      isBust = True
    if(int(calcValue(dealersHand)>21)):
      isDealerBust=True

    if (calcValue(playerAndCards[y]) > calcValue(dealersHand) and isBust==False):
      scoreLabel = Label(playersFrame, text='Win')
      scoreLabel.grid(column=2, row=y)
    elif(isBust==False and isDealerBust==True):
      scoreLabel = Label(playersFrame, text='Win')
      scoreLabel.grid(column=2, row=y)
    elif(calcValue(playerAndCards[y]) == calcValue(dealersHand)):
      scoreLabel = Label(playersFrame, text='Draw')
      scoreLabel.grid(column=2, row=y)
    else:
      scoreLabel = Label(playersFrame, text='Loss')
      scoreLabel.grid(column=2, row=y)



  dealersScoreLabel = Label(dealersFrame, text=calcValue(dealersHand))
  dealersScoreLabel.grid(column=1, row=1)

def hit(deck,whichPlayer,playersHand,playerAndCards,dealersHand):
 global position
 global handCounter
 #Add next card to players hand
 #only deal if value of hand is less then 21 and they have not bust or stuck
 #if player has bust or stuck then handsValid[n] is 1
 if(calcValue(playerAndCards[whichPlayer]) < 21 and handsValid[whichPlayer] ==0):
   playerAndCards[whichPlayer].append(deck[position + 1])
   position = position + 1
   stringNextCard = 'images/' + deck[position] + '.png'
   playersHandToCalcVal = playerAndCards[whichPlayer].copy()
   calcValue(playersHandToCalcVal)
   nextCard = PhotoImage(file=stringNextCard)
   nextCard = nextCard.subsample(2)
   nextCardLabel = Label(playersFrame, image=nextCard)
   nextCardLabel.image = nextCard
   nextCardLabel.grid(column=len(playerAndCards[whichPlayer]) + 5, row=whichPlayer)
   labelValue = Label(playersFrame, text=calcValue(playersHandToCalcVal))
   labelValue.grid(column=6, row=whichPlayer)
   handsValid[whichPlayer] = 0

   if int(calcValue(playersHandToCalcVal)) > 21:
     handScore[whichPlayer] = "Bust"
     labelValue['text'] = "Bust"
     handsValid[whichPlayer] = 1

   if int(calcValue(playersHandToCalcVal)) == 21:
     handsValid[whichPlayer] = 1

   handCounter = handCounter + int(str(handsValid[whichPlayer]))

   if (handCounter == int(numberOfHands())):
     dealer(dealersHand,playerAndCards,deck)

def stick(whichPlayer,playerAndCards,dealersHand,deck):
  global handCounter
  handScore[whichPlayer]=calcValue(playerAndCards[whichPlayer])
  handsValid[whichPlayer] = 1
  handCounter = handCounter + int(str(handsValid[whichPlayer]))
  if (handCounter==int(numberOfHands())):

    if (handCounter == int(numberOfHands())):
      dealer(dealersHand,playerAndCards,deck)


def gamePlay():
  global position
  global handScore
  global handsValid
  global handCounter
  handScore = []
  handsValid = []
  handCounter = 0
  for y in range(0, int(numberOfHands())):
    handScore.append([])
    handsValid.append(0)

  position = int(numberOfHands()) * 2 + 1
  #Destroy the frame and initlize again
  #Allows for more than one game
  #Reset and valid
  playersFrame.destroy()
  playersFrame.__init__()
  dealersFrame.destroy()
  dealersFrame.__init__()
  tmpDeck = []
  deck = []

  dealersHand = []
  count = -1
  #Add each card of the unshuffled deck into a tmp deck
  # n times(n is the number of decks user wants to play with)
  for x in range(0,int(numberOfDecks())):
    for y in range(0,52):
      tmpDeck.append(initDeck()[y])

  deck = shufDeck(tmpDeck)
  for y in range(2 + 2 * int(numberOfHands())):
    if y == int(numberOfHands()):
      dealersHand.append(deck[y])

    if y == (1 + 2 * int(numberOfHands())):
      dealersHand.append(deck[y])
  for x in range(len(dealersHand)):
    stringFromDealerList = "".join(dealersHand[x])
    stringDealerCard = 'images/' + stringFromDealerList + '.png'

    dealersCard = PhotoImage(file=stringDealerCard)
    dealersCard = dealersCard.subsample(2)

    dealersCardsButton = Label(dealersFrame, image=dealersCard)
    dealersCardsButton.grid(column=x, row=0)
    # For some reason without this image overide only last image in loop is shown
    dealersCardsButton.image = dealersCard



    dealersFrame.pack()
  #PlayerAndCards will be 2d list [player,playerscards]
  #EG.[[H3,C4],[C11,D1]]
  playerAndCards = []

  # Add a list to the playerAndCards depending on user input
  for y in range(int(numberOfHands())):
    playerAndCards.append([])

  playersCards = []

  # playersCards will the seqeuence of PDPD for 1 player
  # 2 player will be PPDPPD
  # Deal to player first , then each player, then dealer.
  # Dealer gets a card at Number of players and 2 + 2*Number of Players
  for y in range(2 + 2 * int(numberOfHands())):
    if y != int(numberOfHands()) and y != 1 + 2 * int(numberOfHands()):
      playersCards.append(deck[y])

  # Add the each players hand to list playerAndCards
  # [0] is player1, [1] is player2 etc
  # The sequence for dealing goes player1,player2 etc
  # count starts at -1 because first list element is zero.
  count = -1
  while (count != len(playersCards) - 1):
    for x in range(int(numberOfHands())):
      count = count + 1
      playersAndCardsNestedList = playerAndCards[x]
      playersAndCardsNestedList.append(playersCards[count])

  for x in range(len(playerAndCards)):
    hitStickFrame = Frame(playersFrame, name=str(x))
    stringPlayersCards = ",".join(playerAndCards[x])
    indivdualCard = stringPlayersCards.split(",")
    for y in range(2):
      stringPlayersHand = str(indivdualCard[y])
      indivdualLocationOfCard = 'images/' + indivdualCard[y] + '.png'
      cardN = PhotoImage(file=indivdualLocationOfCard)
      cardN = cardN.subsample(2)

      playersCardLabel = Label(playersFrame, image=cardN)
      playersCardLabel.grid(column=y + 4, row=x)
      playersCardLabel.image = cardN

      labelValue = Label(playersFrame, text=calcValue(playerAndCards[x]))
      labelValue.grid(column=6, row=x)
      label1 = Label(hitStickFrame , text="Player "+str(x+1))
      label1.grid(column=1,row=x)
      buttonHit = Button(hitStickFrame,text='Hit',command=lambda whichPlayer=x,playerListIndex=indivdualCard:
                                                                                                  hit(deck,
                                                                                                      whichPlayer,
                                                                                                      playerListIndex,
                                                                                                      playerAndCards,
                                                                                                      dealersHand))
      buttonHit.grid(column=3, row=x)
      buttonStick = Button(hitStickFrame , text='Stick', command=lambda whichPlayer=x: stick(whichPlayer,
                                                                                            playerAndCards,
                                                                                             dealersHand,
                                                                                             deck))
      buttonStick.grid(column=4, row=x)
      hitStickFrame.grid(column=1, row=x)

  playersFrame.pack()

def init():
  dealButton = Button(root, text="Deal", command=lambda:gamePlay())
  dealButton.pack()

init()
mainloop()

