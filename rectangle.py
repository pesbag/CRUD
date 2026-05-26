from shape import Shape
class Rectangle(Shape):
    def __init__(self, shape_id, shape_type,length,width):
        """Docstring"""
        super().__init__(shape_id, shape_type="rectangle")
        self._length=length
        self._width=width
    def get_perimeter(self):
        """Docstring"""
        return 2*self._width+2*self._length

    def get_area(self):
        """Docstring"""
        return self._length*self._width