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

    def find_id_to_shape(self,all_data):
        logger.info("get to find_id_to_shape function")
        if not all_data:
            logger.info("there is no shapes so define the first shape new id to 1")
            new_id = 1
        else:
            new_id=max([shape["shape_id"] for shape in all_data]) + 1
            logger.info("find new id for shape")
        return new_id

    def get_rectangle(self):
        width = input("please enter width of rectangle\n")
        length = input("please enter length of rectangle\n")
        try:
            return {"width": int(width), "length": int(length)}
        except ValueError:
            logger.exception(f"Error: the values {width},{length} illegal")
            raise

    def get_circle(self):
        radius = input("please enter radius of circle\n")
        try:
            return {"radius": int(radius)}
        except ValueError:
            logger.exception(f"Error: the value {radius} illegal")
            raise

    def get_square(self):
        side = input("please enter side of square\n")
        try:
            return {"side": int(side)}
        except ValueError:
            logger.exception(f"Error: the value {side} illegal")
            raise

    def create_shape(self, shape):
        """
        creating object of specific shape
        :param shape: the specific shape to create
        :return:
        """
        logger.info("enter to create shape")
        shapes_dict={"circle":{"class":Circle, "input_func":self.get_circle},
                     "square":{"class":Square,"input_func":self.get_square},
                   "rectangle":{"class":Rectangle,"input_func":self.get_rectangle}}
        # load to the list the exists objects for add them the new variables
        self.shapes = self.load_from_json()
        logger.info("loaded the json file to shapes list")
        # find the type of object to create from the objects dictionary
        try:
            target_type=shapes_dict[shape]
        except KeyError:
            logger.exception(f"Error shape class {shape} was not found")
            raise
        # start the function of the shape object to get the relevant parameters
        shape_params_func=target_type["input_func"]()
        # find a uniq id for the new shape
        new_shape_id = self.find_id_to_shape(self.shapes)
        # create the new object needed including the uniq id and the relevant parameters
        new_shape_object=target_type["class"](new_shape_id,**shape_params_func)
        # add the new object to the objects list
        # print(new_shape_object)
        self.shapes.append(new_shape_object)
        # print(self.shapes)
        logger.info("add the new object to the objects list")
        # save it to json file
        self.save_to_json()
        logger.info("save it to json file")

    def get_all_shapes(self):
        """
        get all shapes to user
        :return: list of shapes
        """
        all_shapes=self.load_from_json()
        logger.info("load the shapes from json file")
        for s in all_shapes:
            print(s)

    def update_shape(self, shape_id, new_data):
        """
        get an id of shape and update the shape values
        :param shape_id: shape to change the values
        :param new_data: new data to update the shape
        :return:
        """
        logger.info("enter to update shape")
        self.shapes = self.load_from_json()
        for shape in self.shapes:
            if shape["shape_id"] == shape_id:
                for key, value in new_data.items():
                    if key in shape:
                        shape[key] = value
                self.save_to_json()
                print(f"Shape {shape_id} updated successfully!")
                return
        print(f"Error: shape with id {shape_id} not found")
        pass

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
        self.shapes = [s for s in self.shapes if s["shape_id"] != shape_id]
        logger.info("create new list which not include the id remove")
        # save the new list to the json file
        self.save_to_json()
        print(f"Shape with id: {shape_id} deleted successfully")

    def save_to_json(self):
        """
        save the shapes to json
        :return:
        """
        logger.info("enter to save_to_json")
        try:
            with open("shapes.json","w",encoding="utf-8") as f:
                dict_shapes = [s if isinstance(s, dict) else s.to_dict() for s in self.shapes]

                json.dump(dict_shapes, f, indent=4, ensure_ascii=False)
                logger.info("Success to update json file")

        except Exception as e:
            logger.exception(f"Error: failed to write to file: {e}")
            raise

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
            logger.exception("Error: The json file was not found")
            data = []
        except json.JSONDecodeError:
            logger.info("Error: cannot read the json file, it possible to have the first time of writing to the json file")
            data = []
        return data

def main():
    c=ShapeManager()
    # print(c.create_shape("rectangle"))
    print(c.create_shape("circle"))
    # c.get_all_shapes()
    # c.delete_shape(3)
    # c.delete_shape(6)
    # c.get_all_shapes()
if __name__ == '__main__':
    main()