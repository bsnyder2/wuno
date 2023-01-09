from cards import Card


class TextInput:
    def __init__(self, prompt, min=None, max=None):
        self.PROMPT = prompt
        self.MIN = min
        self.MAX = max

    def get_bool(self):
        while True:
            word = input(f"> {self.PROMPT} (y/n): ").strip().lower()
            if word == "y":
                return True
            if word == "n":
                return False

    def get_int(self):
        while True:
            n = input(f"> {self.PROMPT} (n): ").strip()
            if (self.MIN != None and int(n) < self.MIN) or (self.MAX != None and int(n) > self.MAX):
                continue
            return n

    def get_card(self):
        while True:
            letter = input(f"> {self.PROMPT}: ").strip().lower()
            if len(letter) != 1:
                continue
            return Card(letter)
