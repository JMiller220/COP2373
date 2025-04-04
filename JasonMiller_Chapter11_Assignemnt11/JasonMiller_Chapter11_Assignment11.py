# This program deals 5 cards to the user and allows them to replace
# any unwanted cards.
import random

class Deck:

    def __init__(self, size):
        # Creates a list of cards
        self.card_list = [i for i in range(size)]

        # The cards currently dealt in a users hand
        self.cards_in_play_list = []

        # Any cards that are removed
        self.discards_list = []

        # Shuffles the cards
        random.shuffle(self.card_list)

    def deal(self):
        # Happens if there are no more cards to be dealt
        if len(self.card_list) < 1:
            # Shuffles the discarded cards
            random.shuffle(self.discards_list)

            # puts all cards back into the deck
            self.card_list = self.discards_list

            # Resets the discard pile
            self.discards_list = []
            print("Reshuffling...")

        # Takes off the top card
        new_card = self.card_list.pop()

        # Gives the top card to the user
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        # Discards all cards into the discard pile
        self.discards_list += self.cards_in_play_list

        # Clears each users hand
        self.cards_in_play_list.clear()


def main():
    # Creates a deck of 52 cards
    my_hand = Deck(52)

    # Deals 5 cards to the user
    for i in range(5):
        my_hand.deal()

    # Shows the user their current hand
    print(f"Your hand is: ", end='--> ')
    for i in my_hand.cards_in_play_list:
        print(i, end=" ")
    print()

    # Prompts the user to replace cards
    replace = input("Which cards do you want replace (1-5)?: ").split()

    # Calls and holds the replaced_cards function
    new_hand = replace_cards(my_hand, replace)

    # Shows user their new hand
    print("--" * 20)
    print(f"Your new hand is: ", end="--> ")
    for i in new_hand:
        print(i, end=" ")
    print()


def replace_cards(my_hand, discard):
    # Loops through the cards the user wishes to replace
    for card in discard:
        # Makes the card an int to be used as an index
        card = int(card)

        # Checks for valid cards only
        if 0 < card <= 5:
            # Decreases the index by 1
            card -= 1

            # Removes the desired card
            my_hand.cards_in_play_list.pop(card)

            # Deals a new card in the old cards spot.
            my_hand.cards_in_play_list.insert(card, my_hand.deal())

            # Removes the last card (A duplicate of the new dealt card)
            my_hand.cards_in_play_list.pop()

        else:
            # Catches any invalid card indexes
            print()
            print("Invalid. Must select a card (1-5)")
            exit(0)

    # Returns the new users hand.
    return my_hand.cards_in_play_list


if __name__ == "__main__":
    main()