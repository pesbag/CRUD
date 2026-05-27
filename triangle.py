from shape import Shape
class Triangle(Shape):
    def __init__(self,shape_id,shape_type,base,height,third_side):
        """Docstring"""
        super().__init__(shape_id,shape_type="triangle")
        self._base=base
        self._height=height
        self._third_side=third_side
    def get_perimeter(self):
        """Docstring"""
        return self._third_side+self._height+self._base
    def get_area(self):
        """Docstring"""
        return (self._base*self._height)/2
