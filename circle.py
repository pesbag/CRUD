from shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self,shape_id, shape_type, radius):
        """Docstring"""
        super().__init__(shape_id, shape_type="circle")
        self._radius=radius
    def get_area(self):
        """Docstring"""
        return (self._radius**2)*pi
    def get_perimeter(self):
        """Docstring"""
        return 2*pi*self._radius