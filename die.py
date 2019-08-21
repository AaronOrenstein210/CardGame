from random import randrange

class die:
    def __inti__ (self):
        self.val = 0

    def roll(self):
        self.val = randrange (6) + 1
