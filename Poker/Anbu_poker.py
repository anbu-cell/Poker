# Name        : Poker Simulation
# Programmer  : Anbuselvan Ragunathan
# Date        : April 10, 2022
# Description : The program will simulate a game
#               of poker. It will determine which
#               of the two players are the winner based.
#               on which hand is stronger. One round of
#               a tie breaker will be used when needed.
#               Cards are dealt in alternating order.
#               This program does not give the option to switch
#               cards.

# Importing the classes from standard_deck.py and poker_classes.py
from standard_deck import *
from poker_classes import *


### START OF PROGRAM ###

# Main function to start the poker simulation
def main():
        # Structuring a while loop to allow the player to continue the game at will
        game = True
        while (game):
            # Prompting the user to play or quit
            user_input = input("Enter [Y] to play poker or [N] to quit: ")
            # Exception handling
            if (user_input != "Y" and user_input != "N"):
                print ("Invalid input!")
                user_input = input("Enter [Y] to play poker or [N] to quit: ")
            # If the user enter "N", the program ends
            elif (user_input == "N"):
                print("Thanks for playing!")
                game = False
            # If the user clicks "Y", the poker simulation begins
            elif (user_input == "Y"):
                print ("\n")
                poker = Hand()
                player = Game()
                player.determine_hand_type()
                player.determine_winner()

# Calling the main function to start the program
main()

### END OF PROGRAM ###
