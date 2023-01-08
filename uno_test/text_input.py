class TextInput:
    def __init__(self, prompt, min=None, max=None):
        self.prompt = prompt
        self.min = min
        self.max = max

    def get_bool(self):
        while True:
            word = input(f"> {self.prompt} (y/n): ").strip().lower()
            if word == "y":
                return True
            if word == "n":
                return False

    def get_int(self):
        while True:
            n = input(f"> {self.prompt} (n): ").strip().lower()
            if (self.min != None and int(n) < self.min) or (self.max != None and int(n) > self.max):
                continue
            return n