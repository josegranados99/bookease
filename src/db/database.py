from abc import ABC,abstractmethod

class DatabaseAbstractFactory(ABC):
    @abstractmethod
    def connect(self):
        pass

             