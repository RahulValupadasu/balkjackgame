# balkjackgame
#creating a deck of cards using collections module
import random
from collections import namedtuple
card = namedtuple('card',['suite','value'])
suites = ['diamond','hearts','spades','clubs']
values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
cards = [card(suite,value) for suite in suites for value in values]

#shuffling a deck of cards
random.shuffle(cards)

#function to define the number of chips in player1
noOfChips = int(input("please enetr and give the amount you want to convert into gamming chips" ))
bet = int(input('please place the bet'))
if bet<=noOfChips:
    pass
else:
    print('sorry you dont have enough chips, please purchase the chips and add them')
    raise SystemExit
    

player1Cards = []
dealerCards = []
#creating a player 1 class
class Player1:
    def __init__(self):
        for x in range(0,2):
            player1Cards.append(cards[random.randint(0,len(cards)-1)])
        print('your cards are:',player1Cards)
        
#creating a dealer class
class Dealer():
    def __init__(self):
        for y in range(0,2):
            dealerCards.append(cards[random.randint(0,len(cards)-1)])
        print('one of the dealer cards are:',dealerCards[0])
            
dealer = Dealer()#calling dealer class
player1 = Player1()#calling player class

#function defining cards value of player1
def handValueOfPlayer1():
    a=0
    sum=0
    while a<=len(player1Cards)-1:
        sum+=player1Cards[a].value
        a+=1
    return sum
#print(handValueOfPlayer1())

#function defining cards value of dealer
def handValueOfDealer():
    a=0
    sum=0
    while a<=len(dealerCards)-1:
        sum+=dealerCards[a].value
        a+=1
    return sum
#print(handValueOfDealer())


while handValueOfPlayer1()<21:
    hit = str(input('do you want to hit and take another card? Then enter yes'))
    if hit=='yes':
        player1Cards.append(cards[random.randint(0,len(cards)-3)])
        print('\nAfter hitting another cards i.e taking another card, \nCards with you are ',player1Cards)
    if hit=='no':
        break
        
if handValueOfPlayer1()>21:
    print('sorry your handvalue has been more than 21!,you are BURST')
    raise SystemExit

if handValueOfPlayer1()==21:
    print("hey congratulations you have won blackjack")
    raise SystemExit
    
while handValueOfDealer()<=17:
    dealerCards.append(cards[random.randint(0,len(cards)-3)])
print("dealer cards at the end are",dealerCards)
    
if handValueOfPlayer1()>handValueOfDealer()and handValueOfDealer()<21:
    print("hey player1 has won the bet")
if handValueOfPlayer1()<handValueOfDealer()and handValueOfDealer()<21:
    print("hey sorry player1 has lost the bet")
        
        
        
    
    
    







    

        

        
        
    

        
         
    
    
    
    
