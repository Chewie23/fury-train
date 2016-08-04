"""
Go Fish game
Text, of course.

TODO
- How to implement the cards?
- AI
- Logic of the game
- A way to have a "pool" of cards. Instance of a "deck"?

Write a program to let the user play Go Fish against a computer opponent. Use the following rules:

    Each player is dealt nine cards to start with.
    On their turn, a player asks their opponent for a given rank (such as threes or kings). A player must already have at least one card of a given rank to ask for more.
        If the opponent has any cards of the named rank, they must hand over all such cards, and the requester can ask again.
        If the opponent has no cards of the named rank, the requester draws a card and ends their turn.
    A book is a collection of every card of a given rank. Whenever a player completes a book, they may remove it from their hand.
    If at any time a player's hand is empty, they may immediately draw a new card, so long as any new cards remain in the deck.
    The game ends when every book is complete. The player with the most books wins.

The game's AI need not be terribly smart, but it should use at least some strategy. That is, it shouldn't choose legal moves entirely at random. 
"""

#maybe make a class?
#That way, it all fits logically

import random

"""
def card_hand(deck_list):
    print ("Do something")
""" 
#Can probably make the same list with a for loop of some kind. Or function. I'll factor this out when I have a working protoype.
card_deck = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2',
            'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2',
            'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2',
            'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2',]
            
random.shuffle(card_deck)

player_hand = []
comp_hand = []

def deal_out(card_deck):
    for n in card_deck:
        if len(player_hand) < 9:
            player_hand.append(n)
            card_deck.remove(n)
        elif len(comp_hand) < 9:
            comp_hand.append(n)
            card_deck.remove(n)

def read_hand(player_hand):
    print (player_hand)

def check_if_book(hand):
    #need to check if there are 4 of the same card, and take it out of the hand and include it as a "point"
    book_dic = {}
    for i in hand:
        if i not in book_dic:
            book_dic[i] = 1
        else:
            book_dic[i] += 1
    
    return book_dic
    
def ask_for_card(player_hand, comp_hand, card_deck):
    card_choice = input("What card do you want to ask for: ")
    
    card_choice = card_choice.upper()
    
    done = False
    while not done:
        if card_choice not in player_hand:
            print("Illegal move. Choose again.")
        else:
            for j in comp_hand:
                if j is card_choice:
                    pass #Need to compare comp's hand with my hand. Then change stuff around. Like add to my hand, delete from comp's hand
    
deal_out(card_deck)
read_hand(player_hand) #works! Gives a hand of cards and subtracts from deck

print (check_if_book(player_hand))

print (comp_hand)
print (card_deck)