#BLACKJACK
import random
import itertools
#user input - new game / cash out (bitch)

#new hand instance
    #initiate(and shuffle) deck. (deck can be a sequential list of cards that
    #get chosen with random.choice())
class Card(object):
    

    suits = ['Spades','Hearts','Diamonds','Clubs']
    values = range(1,11)+['JACK','QUEEN','KING','ACE']
    
    def __init__(self, suit, value):	
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return "%s of %s" % (Card.values[self.value],Card.suits[self.suit])
        

class Deck(object):
    
    def __init__(self):
    # initialize list of cards for a Deck
        self.cards = []
        for suit in range(4):
            for value in range(1,13):
                card = Card(suit,value)
                self.cards.append(card)
                
    def __str__(self):
    #makes human readable string 
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
        
    def shuffle(self):
    #shuffles deck
        random.shuffle(self.cards)
    
class Player(object):
    '''
    player attributes:
        money
        cards
        score
    '''
    
    def __init__(self):
        self.score = 0
        self.money = 200
        self.cards = []
        
    def addScore(self):
        self.score = 0       
        for card in self.cards:
            if card.value <= 10: #for number cards, add one
                self.score += card.value
                self.score += 1  
            elif card.value == '14': #ACE
                self.score += 11
            elif card.value in [11,12,13]: #JACK QUEEN KING
                self.score += 10
        
    def displayHand(self):
        for card in self.cards:
            print str(card), "/ ",
        print "\nScore - ", self.score
   
def displayTable(uName,dealer): 
    uName.addScore()
    dealer.addScore()     
    print "Your hand: " 
    uName.displayHand()
    print "Dealer shows:"
    print str(dealer.cards[0])     
    
def playGame(uName, dealer):
    
    deck = Deck()
    deck.shuffle()
        
    
    uName.cards   = [deck.cards.pop(0),deck.cards.pop(1)]
    dealer.cards  = [deck.cards.pop(0),deck.cards.pop(1)]
    
    bet = input("BET: ")
    
    while True:
        
        displayTable(uName,dealer)
        
        hit = raw_input("'h' to hit, 's' to stay: ")
        
        if hit == 'h':
            uName.cards.append(deck.cards.pop(0))
            uName.addScore()
            if uName.score > 21:
                print "BUST!"
                break
        elif hit == 's':
            break

            
            
    while True:
        if dealer.score < 17:
            print "Dealer hits, ",
            dealer.cards.append(deck.cards.pop(0))
        elif dealer.score >=17:
            break
        dealer.addScore()
        
        
          
    print "\nDealer shows: "
    dealer.displayHand()  
    
    
    print "Final: "
    print "You: ", uName.score
    print "Dealer: ", dealer.score
        
    if dealer.score >= uName.score and dealer.score <=21 or uName.score > 21:
        print "You Lose!"
        uName.money = uName.money - bet
    else:
        print "You Win!"
        uName.money = uName.money + bet
    
    print "$", uName.money
    
    if uName.money < 0:
        print "Broke! Go home."
    
    #compare hands
    
    

def sitAtTable():
    
    uName   = Player()
    dealer  = Player()
    
    while True:
        play = raw_input("What will it be? 'play' or 'cash out': ")
        if play == 'play':
            playGame(uName, dealer)
        else:
            print 'BITCH...'
            break

sitAtTable()
