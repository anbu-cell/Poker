# Name        : Poker Simulation
# Programmer  : Anbuselvan Ragunathan
# Date        : April 10, 2022
# Description : Contains Hand and Game Class 
           
### START OF PROGRAM ###

# Importing the classes from standard_deck.py
from standard_deck import *

# Structuring the Hand class
class Hand():
    # Initializing the cards list
    def __init__ (self):
        self.card_list = []
    # Getting cards to deal from the classes from standard_deck.py
    def deal_card(self):
        card_ref = Game.deck_ref.get_card()
        self.card_list.append(card_ref)

    # Displaying the card names
    def show_hand(self):
        card_names = []
        for card in (self.card_list):
            card_names.append(card.get_name())
        return card_names
    # Displaying the hands
    def get_hand(self):
        return self.card_list

# Structuring the game class
class Game():
    # Calling the deck class to ensure one deck is being used each game
    deck_ref = Deck()
    # Initializing the deck and needed lists and shuffling the cards to start the game
    # Hands for both players are initialized
    def __init__(self):
        Game.deck_ref = Deck()
        Game.deck_ref.shuffle()
        self.counts_one = []
        self.counts_two = []
        self.suit_count = []
        self.hand_one = Hand()
        self.hand_two = Hand()
        self.deal_hands()
    # Hands for both players are dealt in an alternating fashion
    def deal_hands(self):
        for i in range(10):
            if (i % 2 == 0):
                self.hand_one.deal_card()
                print ("Player one hand")
                for j in (self.hand_one.show_hand()):
                    print (j)
                print("\n")
                print ("Player two hand")
                for k in (self.hand_two.show_hand()):
                    print (k)
                print("")
            else:
                self.hand_two.deal_card()
                print ("Player two hand")
                for j in (self.hand_two.show_hand()):
                    print (j)
                print("\n")
                print("Player one hand")
                for k in (self.hand_one.show_hand()):
                    print (k)
                print("")
                # User clicks enter to deal the next card for the next player
            enter = input("Enter any key to deal a card: ")
            print("\n")
                

    # Determining the result of a win or a draw
    def determine_winner (self):
            # Initialzing hands to result variables and giving values to hand types
            result_one = self.hand_type_one
            result_two = self.hand_type_two
            result_dict = {"Straight flush": 1, "Four of a kind": 2, "Full House": 3, "Flush": 4, "Straight": 5, "Three of a kind": 6, "Two Pair": 7, "Pair": 8, "High card": 9}
            strength_hand_one = result_dict[result_one]
            strength_hand_two = result_dict[result_two]
            print ("\n")

            # Determining a winner based on different hand results from the players
            if (strength_hand_one < strength_hand_two):
                print ("Player one wins!")
            elif (strength_hand_one > strength_hand_two):
                print ("Player two wins!")
            # Determining a winner after an instance of the players having the same hand
            elif (strength_hand_one == strength_hand_two):
                # Sorting the values of the cards so that rank can be determined more easily
                self.value_one.sort()
                self.value_two.sort()
                # Determining who wins after both players get a high card, a straight flush, a straight, or a flush
                # Only the strength of the first hand is considered as it is assumed that the second hand has the same type of hand strength
                if (strength_hand_one == 9 or strength_hand_one == 1 or strength_hand_one == 5 or strength_hand_one == 4):
                    # Comparing the last values of each value list (as it is the highest value)
                    # Determining the winner or a tie
                    if (self.value_one[-1] > self.value_two[-1]):
                        print ("Player one wins!")
                    elif (self.value_one[-1] < self.value_two[-1]):
                        print ("Player two wins!")
                    elif (self.value_one[-1] == self.value_two[-1]):
                        print ("Tie after tiebreaker!")
                # Determining who wins after both players get a two pair
                elif (strength_hand_one == 7):
                    # Looping through the list of card values from the first hand to find the first pair instance
                    for i in range(len(self.value_one)-1):
                        if (self.value_one[i] == self.value_one[i+1]):
                            # Setting the first instance of a pair as a temporary comparison value
                            temp_compare_one = self.value_one[i]
                            # Slicing the list from the first pair instance to now find the second pair instance
                            temp_value_one = self.value_one[i:]
                            # Looping through the sliced list to find the second pair
                            for i in range(len(temp_value_one)-1):
                                if (temp_value_one[i] == temp_value_one[i+1]):
                                    # Setting the second instance of a pair as a second temporary comparison value
                                    temp_compare_two = temp_value_one[i]
                                # Comparing the two temporary comparison values and determining which one is greater
                                # The greater of the two is set as the compare_one value
                                if (temp_compare_one > temp_compare_two):
                                    compare_one = temp_compare_one
                                else:
                                    compare_one = temp_compare_two
                    # Looping through the list of card values from the second had to find the first pair instance
                    for i in range(len(self.value_two)-1):
                        if (self.value_two[i] == self.value_two[i+1]):
                            # Setting the first instance of a pair as a temporary comparison value
                            temp_compare_one = self.value_two[i]
                            # Slicing the list from the first pair instance to now find the second pair instance
                            temp_value_two = self.value_two[i:]
                            # Looping through the sliced list to find the second pair                            
                            for i in range(len(temp_value_two)-1):
                                if (temp_value_two[i] == temp_value_two[i+1]):
                                    # Setting the second instance of a pair as a second temporary comparison value
                                    temp_compare_two = temp_value_two[i]
                                # Comparing the two temporary comparison values and determining which one is greater
                                # The greater of the two is set as the compare_one value
                                if (temp_compare_one > temp_compare_two):
                                    compare_two = temp_compare_one
                                else:
                                    compare_two = temp_compare_two
                    # Comparing the comparison values and determining a winner or a tie 
                    if (compare_one > compare_two):
                        print ("Player one wins!")
                    elif (compare_one < compare_two):
                        print ("Player two wins!")
                    elif (compare_one == compare_two):
                        print ("Tie after tiebreaker!")
                # Determining who wins after both players get either a four of a kind or a pair
                # It is assumed that the logic of comparing the four of a kind and a pair is the same as it is the same tie breaking mechanism
                elif (strength_hand_one == 8 or strength_hand_one == 2):
                    # Looping through the card values of the first hand to find an instance of a pair
                    for i in range(len(self.value_one)-1):
                        if (self.value_one[i] == self.value_one[i+1]):
                            # Setting an instance of a pair to a comparison value
                            compare_one = self.value_one[i]
                    # Looping through the card values of the second hand to find an instance of a pair
                    for i in range(len(self.value_two)-1):
                        if (self.value_two[i] == self.value_two[i+1]):
                            # Setting an instance of a pair to a comparison value
                            compare_two = self.value_two[i]
                    # Comparing the comparison values and determining a winner or a tie
                    if (compare_one > compare_two):
                        print ("Player one wins!")
                    elif (compare_one < compare_two):
                        print ("Player two wins!")
                    elif (compare_one == compare_two):
                        print ("Tie after tiebreaker!")
                # Determining who wins after both players either get a full house or a three of a kind
                # It is assumed that the logic of comparing the full house and a three of a kind is the same as it is the same tie breaking mechanism
                elif (strength_hand_one == 3 or strength_hand_one == 6):
                   # Looping through the card values from the first hand to find the first instnace of a triple
                   for i in range(len(self.value_one)-2):
                       # The i+2 logic is used as in the instance of a triple, it is given that the middle number (i+1) is the same as well
                       if (self.value_one[i] == self.value_one[i+2]):
                           # Setting an instance of a triple to a comparison value
                           compare_one = self.value_one[i]
                   # Looping through the card values of the second hand to find an instance of a triple
                   for i in range(len(self.value_two)-2):
                       if (self.value_two[i] == self.value_two[i+2]):
                           # Setting an instance of a triple to a comparison value
                           compare_two = self.value_two[i]
                   # Comparing the comparison values and determining a winner or a tie 
                   if (compare_one > compare_two):
                       print ("Player one wins!")
                   elif (compare_one < compare_two):
                       print ("Player two wins!")
                   elif (compare_one == compare_two):
                       print ("Tie after tiebreaker!")
    
    # Determining the type of hand
    def determine_hand_type(self):
        # Looping through the hands of both players to get the card values and the suits
        self.value_one = [i.get_value() for i in self.hand_one.get_hand()]
        self.value_two = [i.get_value() for i in self.hand_two.get_hand()]
        suits_one = [i.get_suit() for i in self.hand_one.get_hand()]
        suits_two = [i.get_suit() for i in self.hand_two.get_hand()]
        # Putting the values and the suits into sets to determine how many unique values and suits there are
        # Helps to determine specific hands
        self.unique_value_one = list(set(self.value_one))
        self.unique_value_two = list(set(self.value_two))
        self.unique_suits_one = list(set(suits_one))
        self.unique_suits_two = list(set(suits_two))

        # Looping through the sets to determine the number of instances of unique values
        for i in (self.unique_value_one):
            self.counts_one.append(self.value_one.count(i))
        for i in (self.unique_value_two):
            self.counts_two.append(self.value_two.count(i))
        for i in (self.unique_suits_one):
            self.suit_count.append(suits_one.count(i))
        for i in (self.unique_suits_two):
            self.suit_count.append(suits_two.count(i))
        # Based on the length of the counts list (instances of unique values), hand types are determined
        # Determining a pair if there are 4 unique values
        if (len(self.unique_value_one) == 4):
            self.hand_type_one = "Pair"
        # Determining a two pair or a three of a kind if there are 3 unique values
        elif (len(self.unique_value_one) == 3):
            # Determining a two pair if there are two repeating values in the counts list 
            if (self.counts_one.count(2) == 2):
                self.hand_type_one = "Two Pair"
            # Determining a three of a kind if the above condition is not met
            else:
                self.hand_type_one = "Three of a kind"
        # Determining a four of a kind or a full house if there are 2 unique values
        elif (len(self.unique_value_one) == 2):
            # Determining a four of a kind if there are four repeating values in the counts list
            if (self.counts_one.count(4) == 1):
                self.hand_type_one = "Four of a kind"
            # Determining a full house if the above condition is not met
            else:
                self.hand_type_one = "Full House"
        # Determining a straight flush, a flush, or a high card if there are five unique values
        elif (len(self.unique_value_one) == 5):
            # Looping through the unique values to determine whether if it is a straight flush or a flush
            for i in range(len(self.unique_value_one)):
                # Sorting the unique values
                self.unique_value_one.sort() 
                # If the difference between the highest and lowest terms is 4, then it is a straight
                if (self.unique_value_one[4] - self.unique_value_one[0] == 4):
                    # If there is just one unique suit, then it is a straight flush
                    if (len(self.unique_suits_one) == 1):
                        self.hand_type_one = "Straight flush"
                    # If the above condition is not met, then it is a straight
                    else:
                        self.hand_type_one = "Straight"
            # If the above conditions are not met, then it is a high card
            self.hand_type_one = "High card"
            
        # Based on the length of the counts list (instances of unique values), hand types are determined
        # Determining a pair if there are 4 unique values
        if (len(self.unique_value_two) == 4):
            self.hand_type_two = "Pair"
        # Determining a two pair or a three of a kind if there are 3 unique values
        elif (len(self.unique_value_two) == 3):
            # Determining a two pair if there are two repeating values in the counts list 
            if (self.counts_two.count(2) == 2):
                self.hand_type_two = "Two Pair"
            else:
                # Determining a three of a kind if the above condition is not met
                self.hand_type_two = "Three of a kind"
        # Determining a four of a kind or a full house if there are 2 unique values
        elif (len(self.unique_value_two) == 2):
            # Determining a four of a kind if there are four repeating values in the counts list
            if (self.counts_two.count(4) == 1):
                self.hand_type_two = "Four of a kind"
            # Determining a full house if the above condition is not met
            else:
                self.hand_type_two = "Full House"
        # Determining a straight flush, a flush, or a high card if there are five unique values
        elif (len(self.unique_value_two) == 5):
            # Looping through the unique values to determine whether if it is a straight flush or a flush
            for i in range(len(self.unique_value_two)):
                # Sorting the unique values
                self.unique_value_two.sort()
                # If the difference between the highest and lowest terms is 4, then it is a straight                
                if (self.unique_value_two[4] - self.unique_value_two[0] == 4):
                    # If there is just one unique suit, then it is a straight flush
                    if (len(self.unique_suits_two) == 1):
                        self.hand_type_two = "Straight flush"
                    # If the above condition is not met, then it is a straight
                    else:
                        self.hand_type_two = "Straight"
            # If the above conditions are not met, then it is a high card
            self.hand_type_two = "High card"
        # Displaying the types of hand that both players have after the cards are dealt and the type of hand is determined
        print ("Player one hand type")
        print(self.hand_type_one)
        self.hand_one.get_hand()
        print("\n")
        print("Player two hand type")
        print (self.hand_type_two)
        self.hand_two.get_hand()

### END OF PROGRAM ###
