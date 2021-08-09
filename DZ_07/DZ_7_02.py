from abc import ABC, abstractmethod


class Clothes(ABC):
    @abcstractmethod
    def consumplition(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumplition(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @prorerty
    def consumplition(self):
        return 2 * self.h + 0.3


coat = Coat(50)
costume = Suit(1.96)
print(coat.consumption)
print(costume.consumption)
