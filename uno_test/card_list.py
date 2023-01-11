class CardList:
    def __init__(self):
        self.cards = []

    def __contains__(self, card):
        return card in self.cards

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        output = ""

        if len(self.cards) < 1:
            return "[empty]"
        for card in self.cards:
            output += str(card) + " "

        return output

    def hidden(self):
        output = ""

        if len(self.cards) < 1:
            return "[empty]"
        for card in self.cards:
            output += "[ ] "

        return output

    def letters(self):
        return set([card.LETTER for card in self.cards])

    def add_card(self, card):
        # adds card to hand and sorts alphabetically
        self.cards.append(card)
        self.cards.sort(key=lambda c: c.LETTER)

    def add_from(self, list):
        self.cards.extend(list.cards)
        list.cards = []
        self.cards.sort(key=lambda c: c.LETTER)
