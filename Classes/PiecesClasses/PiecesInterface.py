from abc import ABC, abstractmethod

class Pieces(ABC):

    def move(self):
        pass
    
    def capture(self):
        pass
