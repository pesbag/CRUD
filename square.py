from shape import Shape

import logging

logger=logging.getLogger('shape')
class Square(Shape):
    def __init__(self,shape_id,side,shape_type="square"):
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
        return self._side**2

    def get_perimeter(self):
        """
        :return: the perimeter of the square
        """
        logger.info("enter to get perimetr of square")
        return 4*self._side
    # def get_params(self):
    #     side = input("please enter side of square")
    #     try:
    #         return int(side)
    #     except ValueError:
    #         print(f"Error: the value {side} illegal")

def main():
    s1=Square(5,7)
    print(s1.get_perimeter())
    print(s1.get_area())
if __name__ == '__main__':
    main()