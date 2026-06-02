from shape import Shape

import logging

logger=logging.getLogger('shape')

class Rectangle(Shape):
    def __init__(self, shape_id=None,length=None,width=None,shape_type="rectangle",**kwargs):
        """
        initial rectangle 
        :param shape_id: rectangle id
        :param shape_type: rectangle
        :param length: length of bais
        :param width: length of second bais
        """""
        logger.debug("enter to init of Rectangle class")
        super().__init__(shape_id,shape_type)
        self._length=length
        self._width=width

    def get_perimeter(self):
        """
        :return: the perimeter rectangle
        """
        logger.info("enter to get perimetr of rectangle")
        return round(2*self._width+2*self._length,3)

    def get_area(self):
        """
        :return: the area of triangle
        """
        logger.info("enter to get area of rectangle ")
        return round(self._length*self._width,3)

    def to_dict(self):
        """
        convert the data to dictionary
        :return: dictionary of the data
        """
        logger.info("enter to to_dict of Shape")
        return {"shape_id": self.shape_id, "shape_type": self.shape_type,"width":self._width,"length":self._length
            ,"area":self.get_area(),"perimeter":self.get_perimeter()}

    def __str__(self):
        """
        function for print rectangle data
        :return: rectangle data
        """
        return (f"{super().__str__()}\nWidth:{self._width}\nLength:{self._length}\n"
                f"Area:{self.get_area()}\nPerimeter:{self.get_perimeter()}")

    def get_params(self):
        """
        get a values for the rectangle sides
        :return: dictionary represent the recantgle values
        :raises: ValueError: if one of the values illegal
        """
        logger.info("enter to get_rectangle function")
        width = input("please enter width of rectangle\n").strip()
        self.is_negative_value(width)
        length = input("please enter length of rectangle\n").strip()
        self.is_negative_value(length)
        try:
            return {"shape_type": "rectangle", "width": int(width), "length": int(length)}
        except ValueError:
            logger.exception(f"Error: the values {width},{length} illegal")
            raise

def main():
    s1=Rectangle(3,7,6)
    print(s1.get_perimeter())
    print(s1.get_area())
if __name__ == '__main__':
    main()