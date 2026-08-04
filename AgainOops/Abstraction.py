from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self,r):
        return 3.14*r*r
c=Circle()
print(c.area(2))
