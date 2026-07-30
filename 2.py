# Abstraction
from abc import ABC,abstractmethod
class area(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(area):
    def area(self,r):
        return 3.14*r*r

obj=circle()
print(obj.area(4))