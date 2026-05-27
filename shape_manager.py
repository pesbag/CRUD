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
logger.addHandler(file_handler)

class ShapeManager:
    def __init__(self):
        logger.debug("initialize shape manager")
        self.shapes = []
        self.load_from_json()

    def convert_from_obj_to_dict(self,obj):
        return obj.__dict__

    def find_id_to_shape(self,all_data):
        if not all_data:
            return 1
        return max([shape["id"] for shape in all_data]) + 1

    def get_rectangle(self):
        width = input("please enter width of rectangle")
        length = input("please enter length of rectangle")
        try:
            # return int(width),int(length)
            return {"width": int(width), "length": int(length)}
        except ValueError:
            print(f"Error: the values {width},{length} illegal")

    def get_circle(self):
        radius = input("please enter radius of circle")
        try:
            # return (int(radius),)
            return {"radius": int(radius)}
        except ValueError:
            print(f"Error: the value {radius} illegal")

    def get_square(self):
        side = input("please enter side of square")
        try:
            return {"side": int(side)}
        except ValueError:
            print(f"Error: the value {side} illegal")

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
        target_type=shapes_dict[shape]
        shape_params_func=target_type["input_func"]()
        shape_id = self.find_id_to_shape(self.shapes)
        new_shape_object=target_type["class"](shape_id,**shape_params_func)
        obj_dict=self.convert_from_obj_to_dict(new_shape_object)
        self.shapes.append(obj_dict)
        self.save_to_json()
        # print(self.shapes)

    def get_all_shapes(self):
        """
        get all shapes to user
        :return: list of shapes
        """
        all_shapes=self.load_from_json()
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
        # existing_data = self.load_from_json()
        # if not existing_data:
        #     existing_data=[]
        # existing_data.append(shape_dict)
        try:
            with open("shapes.json","w",encoding="utf-8") as f:
                json.dump(self.shapes, f, indent=4, ensure_ascii=False)
                print("Success to save the shape!")
        except Exception as e:
            print(f"Error: failed to write to file: {e}")

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
            data=[]
        except json.JSONDecodeError:
            print("Error: cannot read the json file")
            data=[]
        return data
def main():
    c=ShapeManager()
    # print(c.create_shape("rectangle"))
    print(c.create_shape("circle"))
    c.get_all_shapes()
if __name__ == '__main__':
    main()