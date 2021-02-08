import random
from random import choices
from string import ascii_uppercase, digits

class Robot:
    def __init__(self):
        random.seed()
        self.name =  ''.join(choices(ascii_uppercase, k=2)) + ''.join(choices(digits, k=3))

    def reset(self):
        random.seed()
        self.name = ''.join(choices(ascii_uppercase, k=2)) + ''.join(choices(digits, k=3))

#Used from pat-pams solution exercism.io
