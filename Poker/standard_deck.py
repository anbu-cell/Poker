# Name       : Standard Deck file for Poker Hands 
# Programmer : 
# Date       : Mar 30 2022
# Description: Contains Card Class and Deck classes


import random

class Card():
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.card_name = rank + ' of ' + suit #Build and store name
        self.value = value

    def get_name(self):
        return self.card_name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Deck():
    SUIT_TUPLE = ("Diamonds", "Clubs", "Hearts", "Spades")
    # Dictionary maps each card rank to a value for a standard deck
    STANDARD_DICT = {"Ace":1, "2":2, "3":3, "4":4, "5":5,
                                  "6":6, "7":7, "8": 8, "9":9, "10":10,
                                  "Jack":11, "Queen":12, "King":13}

    def __init__(self):
        self.starting_deck_list = []
        self.playing_deck_list = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in Deck.STANDARD_DICT.items():
                new_card = Card(rank, suit, value)
                self.starting_deck_list.append(new_card)

    def shuffle(self):
        # Copy the starting deck and save it in the playing deck list
        self.playing_deck_list = self.starting_deck_list.copy()
        random.shuffle(self.playing_deck_list)

    def get_card(self):
        if (len(self.playing_deck_list) == 0):
            raise IndexError("No more cards")
        # Pop one card off the deck and return it
        new_card = self.playing_deck_list.pop()  
        return new_card

    def return_card(self, new_card):
        # Put a card back into the deck
        self.playing_deck_list.insert(0, new_card)


#Test code
if (__name__ == "__main__"):
    # Main code to test the Card and Deck classes
    print ("Test Card class")
    test_card = Card("Ace", "Diamonds", 1)
    print (test_card.get_name () )
    print (test_card.get_value () )
    print (test_card.get_suit () )
    print (test_card.get_rank () )

    print ("\nTest Deck class")
    deck_ref = Deck()
    deck_ref.playing_deck_list = deck_ref.starting_deck_list
    for i in range(52):
        new_card = deck_ref.get_card()
        print("Name: ", new_card.get_name(), "  Value:", new_card.get_value())

