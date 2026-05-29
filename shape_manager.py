import logging
import  json

from shape import Shape
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

logger=logging.getLogger('shape')
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler=logging.FileHandler('shape.log',encoding="utf-8")
file_handler.setFormatter(formatter)
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class ShapeManager:
    def __init__(self):
        logger.debug("initialize shape manager")
        self.shapes = []
        self.load_from_json()

    def get_shape_by_id(self, shape_id):
        """
        find the object of shape by shape_id
        :param shape_id: the shape object to find
        :return: shape object if exists, None else
        """
        self.shapes = self.load_from_json()
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                return shape
        return None

    def find_id_to_shape(self,all_data):
        """"
        find a uniq id for new shape.
        :return: 1 if there is no any shapes, else return the maximum exists id+1
        """
        logger.info("get to find_id_to_shape function")
        if not all_data:
            logger.info("there is no shapes so define the first shape new id to 1")
            new_id = 1
        else:
            new_id=max([shape.shape_id for shape in all_data]) + 1
            logger.info("find new id for shape")
        return new_id
    def is_negative_value(self,val):
        """
        check if the value length is negative
        :param val: the length
        :raise:
        """
        if len(val)<=1:
            return
        if val[0]=="-":
            logger.error(f"Error: length of side cannot be negative ({val})")
            print(f"Error: length of side cannot be negative ({val})")
            raise ValueError("Length cannot be negative")

    def get_rectangle(self):
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
            return {"width": int(width), "length": int(length)}
        except ValueError:
            logger.exception(f"Error: the values {width},{length} illegal")
            raise

    def get_circle(self):
        """
        get a radius for the circle
        :return: dictionary when the key is 'radius' and the value is integer represent the radius
        :raises:ValueError:
        """
        logger.info("enter to get_circle function")
        radius = input("please enter radius of circle\n").strip()
        self.is_negative_value(radius)
        try:
            return {"radius": int(radius)}
        except ValueError:
            logger.exception(f"Error: the value {radius} illegal")
            raise

    def get_square(self):
        """
        get a side value for the square
        :return: dictionary represent the square values
        :raises: ValueError: if one of the values illegal
        """
        logger.info("enter to get_square function")
        side = input("please enter side of square\n").strip()
        self.is_negative_value(side)
        try:
            return {"side": int(side)}
        except ValueError:
            logger.exception(f"Error: the value {side} illegal")
            raise

    shapes_dict = {"circle": {"class": Circle, "input_func": get_circle},
                   "square": {"class": Square, "input_func": get_square},
                   "rectangle": {"class": Rectangle, "input_func": get_rectangle}}

    def create_shape(self, shape):
        """
        creating object of specific shape
        :param shape: the specific shape to create
        :return:
        """
        logger.info("enter to create shape")
        # load to the list the exists objects for add them the new variables
        self.shapes = self.load_from_json()
        logger.info("loaded the json file to shapes list")

        # find the type of object to create from the objects dictionary
        try:
            target_type=self.shapes_dict[shape]
        except KeyError:
            logger.exception(f"Error shape class {shape} was not found")
            raise
        # start the function of the shape object to get the relevant parameters
        try:
            shape_params_func=target_type["input_func"](self)
        except ValueError:
            logger.exception("ValueError: the values should be a positive integer")
            print("Error: the value is illegal, the values should be a positive integer")
            raise

        # find a uniq id for the new shape
        new_shape_id = self.find_id_to_shape(self.shapes)
        # create the new object needed including the uniq id and the relevant parameters
        new_shape_object=target_type["class"](new_shape_id,**shape_params_func)
        # add the new object to the objects list
        self.shapes.append(new_shape_object)
        logger.info("add the new object to the objects list")
        # save it to json file
        self.save_to_json()
        logger.info("save it to json file")

    def get_all_shapes(self):
        """
        get all shapes to user
        :return: list of shapes
        """
        logger.info("enter to get_all_shapes function")
        all_shapes=self.load_from_json()
        logger.info("load the shapes from json file in get_all_shapes function")
        for s in all_shapes:
            print(s,end="\n")

    def update_shape(self, shape_id, new_data):
        """
        get an id of shape and update the shape values
        :param shape_id: shape to change the values
        :param new_data: new data to update the shape
        :return:
        """
        logger.info("enter to update_shape function")
        self.shapes = self.load_from_json()

        is_found = False
        shape=self.get_shape_by_id(shape_id)

        if isinstance(shape, Circle):
            is_found = True
            if "radius" in new_data:
                shape._radius = new_data["radius"]
        elif isinstance(shape, Square):
            is_found = True
            if "side" in new_data:
                shape._side = new_data["side"]
        elif isinstance(shape, Rectangle):
            is_found = True
            if "width" in new_data:
                shape._width = new_data["width"]
            if "length" in new_data:
                shape._length = new_data["length"]

        if not is_found:
            logger.error(f"Error: shape with id {shape_id} not found")
            print(f"Error: shape with id {shape_id} not found")
            return
        self.save_to_json()
        print(f"shape {shape_id} updated successfully")

    def delete_shape(self, shape_id):
        """
        delete specific shape
        :param shape_id: shape to delete
        :return:
        """
        logger.info("enter to delete shape")

        # load the json file to list of dictionaries
        self.shapes = self.load_from_json()
        # create a new list with not including the shape id to remove
        is_found=False
        for index,shape in enumerate(self.shapes):
            if shape.shape_id==shape_id:
                is_found = True
                self.shapes.pop(index)
                print(f"Shape with id: {shape_id} deleted successfully")
                break
        if not is_found:
            logger.error(f"error: the shape id: {shape_id} was not found")
            print(f"Error: shape id:+ {shape_id} does not exist in the system")
        # save the new list to the json file
        self.save_to_json()


    def save_to_json(self):
        """
        save the shapes to json
        :return:
        """
        logger.info("enter to save_to_json")
        try:
            with open("shapes.json","w",encoding="utf-8") as f:
                dict_shapes = [s.to_dict() for s in self.shapes]
                json.dump(dict_shapes, f, indent=4, ensure_ascii=False)
                logger.info("Success to update json file")
        except Exception as e:
            logger.exception(f"Error: failed to write to file: {e}")
            raise

    def load_from_json(self):
        """
        load the data shapes from the json file
        :return: object list if exists or empty list if the json file is empty
        """
        logger.info("enter to load_from_json")
        try:
            with open("shapes.json","r",encoding="utf-8") as f:
                data=json.load(f)
        except FileNotFoundError:
            logger.exception("Error: The json file was not found")
            data = []
        except json.JSONDecodeError:
            logger.info("Error: cannot read the json file, it possible to have the first time of writing to the json file")
            data = []
        object_lst=self.convert_data_to_objects(data)
        return object_lst

    def convert_data_to_objects(self,data_dict):
        """
        convert the list of dictionary to list of objects
        :param data_dict: list of dictionary
        :return: list of objects
        """
        obj_lst=[]
        for d in data_dict:
            shape_data=d.copy()
            shape_id=shape_data.pop("shape_id")
            shape_type=shape_data.pop("shape_type")
            if shape_type in self.shapes_dict:
                shape_class=self.shapes_dict[shape_type]["class"]
                obj=shape_class(shape_id,**shape_data)
                obj_lst.append(obj)
        return obj_lst



def main():
    c=ShapeManager()
    print(c.create_shape("rectangle"))
    print(c.create_shape("circle"))
    # c.get_all_shapes()
    # c.delete_shape(7)
    # c.delete_shape(6)
    c.get_all_shapes()
    # c.update_shape(1)
if __name__ == '__main__':
    main()