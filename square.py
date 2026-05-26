from shape import Shape
class Square(Shape):
    def __init__(self,shape_id,shape_type,side):
        super().__init__(shape_id,shape_type="square")
        self._side=side
    def get_area(self):
        return self._side**2
    def get_perimeter(self):
        return 4*self._side