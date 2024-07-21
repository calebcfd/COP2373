#This program uses a Deck object to simulate a deck of cards. The main function draws a hand of five cards and gives the user a chance to redraw any of the cards.

import random
import re

#Deck class is the same as in the textbook except for the new method discard()
class Deck():

    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)
    
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card
    
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

    #Function discard() takes an integer, adds it to the discards_list, and removes it from the cards_in_play_list.
    def discard(self, card):
        self.discards_list.append(card)
        self.cards_in_play_list.remove(card)


#Function main() creates a hand of 5 cards, reads it to the user, takes input for cards to replace, and shows the new hand.
def main():

    #Variable ranks is a list that stores the possible values for a card.
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    #Variable suits is a list that holds the possible card suits.
    suits = ['clubs', 'diamonds', 'hearts', 'spades' ]
    #Variable my_deck is the Deck object that function main() will use.
    my_deck = Deck(52)

    #Variable hand is a list that holds 5 cards.
    hand = [my_deck.deal(), my_deck.deal(), my_deck.deal(), my_deck.deal(), my_deck.deal()]

    #This loop reads off each card in hand.
    for card in hand:

        r = card % 13
        s = card // 13
        print(ranks[r], 'of', suits[s])

    #Variable i gets input for which cards to replace.
    i = input("Enter numbers to indicate which cards will be replaced during draw phase: ")

    #Variable d creates a list of all single digits in i
    d = re.findall(r"\d", i)

    #For each number in d, call the discard method on it and replace that card by drawing a new one.
    for x in d:

        x = int(x)
        
        my_deck.discard(hand[x-1])
        hand[x-1] = my_deck.deal()


    #Print the new hand to the user.
    print("Your new hand is:")

    for card in hand:

        r = card % 13
        s = card // 13
        print(ranks[r], 'of', suits[s])

#Call main()
main()