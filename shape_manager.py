import logging
logger=logging.getLogger('shape')
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s | %(levelname)s | %()s')
file_handler=logging.FileHandler('shape.log',encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        pass

    def get_all_shapes(self):
        pass

    def update_shape(self, shape_id, new_data):
        pass

    def delete_shape(self, shape_id):
        pass

    def save_to_json(self):
        pass

    def load_from_json(self):
        pass