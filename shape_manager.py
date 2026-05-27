import logging
import  json

from shape import Shape
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

logger=logging.getLogger('shape')
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s | %(levelname)s | %()s')
file_handler=logging.FileHandler('shape.log',encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class ShapeManager:
    def __init__(self):
        logger.debug("initialize shape manager")
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        """
        creating object of specific shape
        :param shape: the specific shape to create
        :return:
        """
        logger.info("enter to create shape")
        lst_shape=[Circle,Square,Rectangle,Triangle]
        for s in lst_shape:
            if str(s).lower()==shape:
                self.shapes.append(s.get_params())
    def get_all_shapes(self):
        """
        get all shapes to user
        :return: list of shapes
        """
        pass

    def update_shape(self, shape_id, new_data):
        """
        get an id of shape and update the shape values
        :param shape_id: shape to change the values
        :param new_data: new data to update the shape
        :return:
        """
        logger.info("enter to update shape")
        pass

    def delete_shape(self, shape_id):
        """
        delete specific shape
        :param shape_id: shape to delete
        :return:
        """
        logger.info("enter to delete shape")
        pass

    def save_to_json(self):
        """
        save the shapes to json
        :return:
        """
        logger.info("enter to save_to_json")
        pass

    def load_from_json(self):
        """
        load the data shapes from the json file
        :return:
        """
        logger.info("enter to load_from_json")
        try:
            with open("shapes.json","r",encoding="utf-8") as f:
                data=json.load(f)
        except FileNotFoundError:
            print("Error: The json file was not found")
            data={}
        except json.JSONDecodeError:
            print("Error: cannot read the json file")
            data={}
        return data