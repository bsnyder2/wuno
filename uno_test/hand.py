from cards import Card


class Hand:
    def __init__(self):
        self.cards = []

    def __contains__(self, card):
        return card in self.cards

    def __str__(self):
        output = ""

        if len(self.cards) < 1:
            return "[empty]"
        for card in self.cards:
            output += str(card) + " "

        return output

    def letters(self):
        return set([card.LETTER for card in self.cards])

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("Invalid object added to hand")

        # adds card to hand and sorts alphabetically
        self.cards.append(card)
        self.cards.sort(key=lambda c : c.LETTER)

    def remove_card(self, card):
        self.cards.remove(card)
