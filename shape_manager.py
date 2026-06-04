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

    shapes_dict = {"circle": Circle,
                   "square": Square,
                   "rectangle": Rectangle}

    def create_shape_1(self,shape_data):
        # self.shapes = self.load_from_json()
        self.load_from_json()
        shape_type=shape_data["shape_type"]
        if shape_type not in self.shapes_dict:
            return None
        else:
            params = shape_data.copy()
            params.pop("shape_type", None)
            params.pop("shape_id", None)
            new_shape_id = self.find_id_to_shape(self.shapes)
            shape_class=self.shapes_dict[shape_type]
            new_shape_object = shape_class(new_shape_id, **params)
            print(type(new_shape_object))
            self.shapes.append(new_shape_object)
            print("self.shapes in create_shape_1",self.shapes)
            self.save_to_json()
            logger.info(f"Successfully created and saved {shape_type} with ID {new_shape_id}")

            return new_shape_object

    def analys_param_of_shape(self,shape):
        # find the type of object to create from the objects dictionary
        try:
            target_type = self.shapes_dict[shape]
        except KeyError:
            logger.exception(f"Error shape class {shape} was not found")
            raise
        # start the function of the shape object to get the relevant parameters
        try:
            shape_params_func = target_type["input_func"](self)
        except ValueError:
            logger.exception("ValueError: the values should be a positive integer")
            print("Error: the values is illegal, the values should be a positive integer")
            raise
        # find a uniq id for the new shape
        new_shape_id = self.find_id_to_shape(self.shapes)
        # create the new object needed including the uniq id and the relevant parameters
        new_shape_object = target_type["class"](new_shape_id, **shape_params_func)
        # add the new object to the objects list
        self.shapes.append(new_shape_object)
        logger.info("add the new object to the objects list")

    def get_all_shapes(self):
        """
        get all shapes to user
        :return: list of shapes
        """
        logger.info("enter to get_all_shapes function")
        all_shapes=self.load_from_json()
        logger.info("load the shapes from json file in get_all_shapes function")
        return all_shapes
        # for s in all_shapes:
            # print(s,end="\n")
            # return s
    def update_shape(self, shape_id, new_data):
        """
        get an id of shape and update the shape values
        :param shape_id: shape to change the values
        :param new_data: new data to update the shape
        :return:
        """
        logger.info("enter to update_shape function")
        # self.shapes = self.load_from_json()
        self.load_from_json()
        print(f'from the server{self.load_from_json()}')
        is_found = False
        # shape=self.get_shape_by_id(shape_id)

        shape = None
        for s in self.shapes:
            if s.shape_id == shape_id:
                shape = s
                break

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
            return False
        self.save_to_json()
        print(f"shape {shape_id} updated successfully")
        return True

    def delete_shape(self, shape_id):
        """
        delete specific shape
        :param shape_id: shape to delete
        :return:
        """
        logger.info("enter to delete shape")

        # load the json file to list of dictionaries
        # self.shapes = self.load_from_json()
        self.load_from_json()
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
        return is_found



    def save_to_json(self):
        """
        save the shapes to json
        :return:
        """
        logger.info("enter to save_to_json")
        print(self.shapes)
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
        # object_lst=self.convert_data_to_objects(data)
        self.shapes=self.convert_data_to_objects(data)
        print("The object list",self.shapes)
        return self.shapes
        # return data

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
                shape_class=self.shapes_dict[shape_type]
                obj=shape_class(shape_id,**shape_data)
                obj_lst.append(obj)
        return obj_lst

    def get_sum_of_all_area(self):
        self.load_from_json()
        total_area=0
        for shape in self.shapes:
            total_area+=shape.get_area()
        return total_area


def main():
    c=ShapeManager()
    # print(c.create_shape("rectangle"))
    # print(c.create_shape("circle"))
    print(c.get_sum_of_all_area())
    # c.get_all_shapes()
    # c.delete_shape(7)
    # c.delete_shape(6)
    c.get_all_shapes()
    # c.update_shape(1)
if __name__ == '__main__':
    main()