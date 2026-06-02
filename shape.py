import logging

logger=logging.getLogger('shape')

class Shape:
    def __init__(self, shape_id, shape_type):
        """
        initial the generic shape
        :param shape_id: shape id
        :param shape_type: type of shapse to initilaize
        """
        logger.debug("enter to  init of Shape class")
        self.shape_id = shape_id
        self.shape_type = shape_type

    def get_area(self):
        """
        get the area of generic shape
        :return: the area
        """
        logger.debug("enter to  get area of Shape")
        pass

    def get_perimeter(self):
        """
       get the perimeter of generic shape
       :return: the perimeter
        """
        logger.debug("enter to  get perimeter of Shape")
        pass

    def to_dict(self):
        """
        convert the data to dictionary
        :return: dictionary of the data
        """
        logger.debug("enter to to_dict of Shape")
        return {"shape_id":self.shape_id,"shape_type":self.shape_type}

    def __str__(self):
        """"
        use to prints the objects
        :return: the object
        """
        return f"\nid:{self.shape_id}\nType:{self.shape_type}"

    def get_params(self):
        """
        get the parameter needed for the shapes
        :return:
        """
        pass

    def is_negative_value(self,val):
        """
        check if the value length is negative
        :param val: the length
        :raise:
        """
        if len(val) <= 1:
            return
        if val[0] == "-":
            logger.error(f"Error: length of side cannot be negative ({val})")
            print(f"Error: length of side cannot be negative ({val})")
            raise ValueError("Length cannot be negative")
