from shape import Shape
# assuming that the hexagon is a regular hexagon
class Hexagon(Shape):
    def __init__(self,shape_id,shape_type,side):
        super().__init__(shape_id,shape_type="hexagon")
        self._side=side
    def get_perimeter(self):
        return 6*self._side
    def get_area(self):
        return (self._side**2)*((3**(1/3))/2)
