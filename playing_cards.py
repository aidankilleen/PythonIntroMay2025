# playing_cards.py

# suit 1=H, 2=S, 3=D, 4=C
# value 1=A, 2=2, 3=3, ..., 10=10, 11=J, 12=Q, 13=K

from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value    #__ indicates this is private

    def get_suit(self):
        return self.__suit
    def get_value(self):
        return self.__value
    def set_suit(self, suit):
        if suit >=1 and suit <= 4:
            self.__suit = suit
        else:
            raise CardError(f"Invalid suit:{suit}")

    def set_value(self, value):
        if value >=1 and value <= 13:
            self.__value = value
        else:
            raise CardError(f"Invalid value:{value}")

    def __str__(self):

        suits = ['','H', 'S', 'D', 'C']
        values = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card = f"{values[self.__value]:>2}{suits[self.__suit]} "

        return card



    # equvalent to toString() in java etc    
    def __str2__(self):
        card = " "
        if self.__value == 1:
            card += "A"
        elif self.__value >= 2 and self.__value <= 10:
            card += str(self.__value)
        elif self.__value == 11:
            card += "J"
        elif self.__value == 12:
            card += "Q"
        elif self.__value == 13:
            card += "K"
        else:
            card += "?"
        
        if self.__suit == 1:
            card += "H"
        elif self.__suit == 2:
            card += "S"
        elif self.__suit == 3:
            card += "D"
        elif self.__suit == 4:
            card += "C"
        else:
            card += "?"
        card += " "
        return card

    def display(self):

        print (self, end="")

class Deck:

    def __init__(self):
        self.cards = []
        
        for s in range(1,5):
            for v in range(1, 14):
                c = Card(s, v)
                self.cards.append(c)

    def display(self):

        for index, card in enumerate(self.cards):
            print (card, end="")

            if index == 12 or index == 25 or index == 38 or index == 51:
                print()

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        # deal the next card
        return self.cards.pop()
        
class CardError(Exception):
    pass



if __name__ == "__main__":

    d = Deck()
    d.shuffle()
    d.display()




    # for s in range(1,5):
    #     for v in range(1, 14):
    #         c = Card(s, v)
    #         c.display()
    #     print()
