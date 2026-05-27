import logging

logger=logging.getLogger('shape')

class Shape:
    counter = 0
    def __init__(self, shape_id, shape_type):
        """
        initial the generic shape
        :param shape_id: shape id
        :param shape_type: type of shpape to initilaize
        """
        logger.debug("enter to Shape class")
        Shape.counter += 1
        self.id = Shape.counter
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
        return {"shape_id":self.id,"shape_type":self.shape_type}
        # json.dump(self.)

    def get_params(self):
        """
        get the parameter needed for the shapes
        :return:
        """
        pass
