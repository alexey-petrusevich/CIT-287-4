from tkinter import *
import tkinter.messagebox as box
import random

root = Tk()
root.geometry("600x400")
root.title("Project 4 (Blackjack)")

numCards = 0
score = 0
aceFlag = False
hasAce = False
balance = 1000
prize = 100
bet = 50

cards = []
suits = (
    "Clubs",
    "Diamonds",
    "Hearts",
    "Spades"
    )
    
names = (
    {"name": "Ace", "value" : 11},
    {"name": "Two", "value" : 2},
    {"name": "Three", "value" : 3},
    {"name": "Four", "value" : 4},
    {"name": "Five", "value" : 5},
    {"name": "Six", "value" : 6},
    {"name": "Seven", "value" : 7},
    {"name": "Eight", "value" : 8},
    {"name": "Nine", "value" : 9},
    {"name": "Ten", "value" : 10},
    {"name": "Jack", "value" : 10},
    {"name": "Queen", "value" : 10},
    {"name": "King", "value" : 10}
    )

btnWidth = 30
btnPadY = 15
btnFont = "Times 16 bold"
lblFont = "Times 18 bold italic"

# functions
######################################################################################
def mainMenu():
    # back to main menu
    playFrame.pack_forget()
    displayFundsFrame.pack_forget()
    mainMenuframe.pack()


def playGame():
    #print("Play the Game")
    # hide main menu and put playGameFrame
    mainMenuframe.pack_forget()
    playFrame.pack()
    # reset cards and shufle
    lblLog.configure(text = "")
    resetCards()
    random.shuffle(cards)
    
    global numCards
    global score
    global aceFlag
    global hasAce
    
    numCards = 0
    score = 0
    aceFlag = False
    hasAce = False
    playerCards = []
    nextCard(playerCards)

    """print("Player cards:")
    for card in playerCards:
        print(card)"""

    btnNextCard.configure(command = lambda: nextCard(playerCards))
    
def displayFunds():
    mainMenuframe.pack_forget()
    displayFundsFrame.pack()
    lblText = "Available funds: " + str(balance);
    lblDisplayFunds.configure(text = lblText)

    
def resetFunds():
    answer = box.askyesno("Reset funds", "Do you want to reset your funds?")
    if answer == 1:
        global balance
        balance = 1000
    
def quitGame():
    var = box.askyesno("Quitting", "Are you sure?")
    if var == 1:
        box.showinfo("Quitting","Thank you for playing blackjack!")
        root.destroy()
    
def nextCard(playerCards):
    global hasAce
    card = cards.pop(0)
    playerCards.append(card)
    global numCards
    global score
    numCards += 1
    appendCardTxt(card)
    # if player has an ace, count every other ace as 1 instead of 11
    if hasAce == True and card["card"]["name"] == "Ace":
        score += 1
    else:
        if card["card"]["name"] == "Ace":
            hasAce = True
        score += card["card"]["value"]
    #print("Score:", score)
    
    if score >= 21:
        global aceFlag
        global balance
        
        if score == 21:
            box.showinfo("Victory!", "You WON the game!")
            balance += prize
        elif aceFlag == False and hasAce == True:
            score -= 10
            #print("Ace - score decreased by 10. New score: ", score)
            aceFlag = True
            return
        elif score > 21:
            box.showinfo("Loss", "You LOST the game!")
            balance -= bet
                
        if balance == 0:
            box.showinfo("Game Over", "Game Over - You are out of funds!")
            root.destroy()
        else:
            #print("balance", balance)
            playAgain = box.askyesno("Play again", "Do you want to play again?")
            if playAgain == 1:
                playGame()
            else:                
                mainMenu()

def appendCardTxt(card):
    lblText = lblLog.cget("text")
    lblText += str(numCards) + ". " + card["card"]["name"] + " of " + card["suit"] + "\n"
    lblLog.configure(text = lblText)
    
def resetCards():
    
    cards.clear()

    for suit in suits:
        for name in names:
            card = {"suit": suit, "card":name}
            cards.append(card)

    """for card in cards:
        print(card)"""
######################################################################################


#######################################
# main frame
#######################################
mainMenuframe = Frame(root)
lblMain = Label(mainMenuframe,
                text = "Blackjack",
                font = lblFont)
btnPlay = Button(mainMenuframe,
                 width = btnWidth,
                 text = "1. Play the Game",
                 font = btnFont,
                 command = playGame)
btnDisplayFunds = Button(mainMenuframe,
                         width = btnWidth,
                         text = "2. Display Available Funds",
                         font = btnFont,
                         command = displayFunds)
btnResetFunds = Button(mainMenuframe,
                       width = btnWidth,
                       text = "3. Reset Funds",
                       font = btnFont,
                       command = resetFunds)
btnQuit = Button(mainMenuframe,
                 width = btnWidth,
                 text = "4. Quit",
                 font = btnFont,
                 command = quitGame)

lblMain.pack()
btnPlay.pack(pady = btnPadY)
btnDisplayFunds.pack(pady = btnPadY)
btnResetFunds.pack(pady = btnPadY)
btnQuit.pack(pady = btnPadY)
#######################################
# play frame
#######################################
playFrame = Frame(root)
lblLog = Label(playFrame,
               text = "",
               font = lblFont)
btnNextCard = Button(playFrame,
                     text = "Next Card",
                     font = btnFont)
btnNextCard.pack(pady = btnPadY)
lblLog.pack(pady = btnPadY);

#######################################
#display funds frame
#######################################
displayFundsFrame = Frame(root)
lblDisplayFunds = Label(displayFundsFrame,
                   text = "",
                   font = lblFont)
btnOk = Button(displayFundsFrame,
                   width = btnWidth,
                   text = "Return to Main Menu",
                   font = btnFont,
                   command = mainMenu
                   )
lblDisplayFunds.pack()
btnOk.pack()

#######################################

mainMenuframe.pack()

# start window
root.mainloop()
