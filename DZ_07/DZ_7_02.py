from abc import ABC, abstractmethod


class Clothes(ABC):
<<<<<<< HEAD
    @abstractmethod
    def consumption(self):
=======
    @abcstractmethod
    def consumplition(self):
>>>>>>> Py_DZ_07
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
<<<<<<< HEAD
    def consumption(self):
=======
    def consumplition(self):
>>>>>>> Py_DZ_07
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

<<<<<<< HEAD
    @property
    def consumption(self):
        return 2 * self.h + 0.3


coat = Coat(46)
costume = Suit(1.6)
=======
    @prorerty
    def consumplition(self):
        return 2 * self.h + 0.3


coat = Coat(50)
costume = Suit(1.96)
>>>>>>> Py_DZ_07
print(coat.consumption)
print(costume.consumption)
