from card_list import CardList


class Hand(CardList):
    

    def remove_card(self, card):
        self.cards.remove(card)
