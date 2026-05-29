from shape import Shape
from math import pi

import logging

logger=logging.getLogger('shape')

class Circle(Shape):
    def __init__(self,shape_id, radius,shape_type="circle",**kwargs):
        """
        initial circle shape
        :param shape_id: circle id
        :param radius: radius of circule
        :param shape_type: circle
        """
        logger.debug("enter to Circle class")
        super().__init__(shape_id, shape_type)
        self._radius=radius

    def get_area(self):
        """
        :return: the area of the circle
        """
        logger.info("enter to get area of circle ")
        return round((self._radius**2)*pi,3)

    def get_perimeter(self):
        """
        :return: the perimeter of the circle
        """
        logger.info("enter to get perimetr of circle ")
        return round(2*pi*self._radius,3)

    def to_dict(self):
        """
        convert the data to dictionary
        :return: dictionary of the data
        """
        logger.debug("enter to to_dict of Shape")
        return {"shape_id": self.shape_id, "shape_type": self.shape_type,"radius":self._radius,"area":self.get_area(),"perimeter":self.get_perimeter()}
    def __str__(self):
        """
        function to print circle data
        :return: the circle data
        """
        return (f"{super().__str__()}\nRadius:{self._radius}\n"
                f"Area:{self.get_area()}\nPerimeter:{self.get_perimeter()}")

def main():
    s1=Circle(5,3)
    print(s1.get_perimeter())
    print(s1.get_area())
if __name__ == '__main__':
    main()