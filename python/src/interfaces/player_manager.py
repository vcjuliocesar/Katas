from abc import ABC,abstractclassmethod

class PlayerManager(ABC):
    
    @abstractclassmethod
    def score(self):
        pass