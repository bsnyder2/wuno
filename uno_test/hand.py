from card_list import CardList


class Hand(CardList):
    def add_from(self, list):
        self.cards.extend(list.cards)
        list.cards = []
        self.cards.sort(key=lambda c: c.LETTER)

    def remove_card(self, card):
        self.cards.remove(card)
