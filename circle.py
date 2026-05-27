from shape import Shape
from math import pi

import logging

logger=logging.getLogger('shape')

class Circle(Shape):
    def __init__(self,shape_id, radius,shape_type="circle"):
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
        return (self._radius**2)*pi
    def get_perimeter(self):
        """
        :return: the perimeter of the circle
        """
        logger.info("enter to get perimetr of circle ")
        return 2*pi*self._radius

def main():
    s1=Circle(5,3)
    print(s1.get_perimeter())
    print(s1.get_area())
if __name__ == '__main__':
    main()