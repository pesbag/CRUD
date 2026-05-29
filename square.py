from shape import Shape

import logging

logger=logging.getLogger('shape')
class Square(Shape):
    def __init__(self,shape_id,side,shape_type="square",**kwargs):
        """
        initial square
        :param shape_id: square id
        :param shape_type: square
        :param side: the length of the bais
        """
        logger.debug("enter to Square class")
        super().__init__(shape_id,shape_type)
        self._side=side

    def get_area(self):
        """
        :return: the area of the square
        """
        logger.info("enter to get area of square ")
        return round(self._side**2,3)

    def get_perimeter(self):
        """
        :return: the perimeter of the square
        """
        logger.info("enter to get perimetr of square")
        return round(self._side * 4, 3)

    def to_dict(self):
        """
        convert the data to dictionary
        :return: dictionary of the data
        """
        logger.debug("enter to to_dict of Shape")
        return {"shape_id": self.shape_id, "shape_type": self.shape_type,"side":self._side,
                "area":self.get_area(),"perimeter":self.get_perimeter()}

    def __str__(self):
        """"
        function to print square data
        :return: the square data
        """
        return (f"{super().__str__()}\nSide:{self._side}\n"
                f"Area:{self.get_area()}\nPerimeter:{self.get_perimeter()}")

def main():
    s1=Square(5,7)
    print(s1.get_perimeter())
    print(s1.get_area())
if __name__ == '__main__':
    main()