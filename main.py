#  https://github.com/pesbag/CRUD.git
# link to git with the server: https://github.com/pesbag/CRUD.git
from logging import exception

import shape_manager
import logging

logger=logging.getLogger('shape')

def show_menu():
     choice=input("\npress 1 to Add shape\n "
          "press 2 to Show all shapes\n "
          "press 3 to Update shape\n "
          "press 4 to Delete shape\n "
          "press 5 to Exit ")

     if not choice.isdigit():
         logger.error(f"Error: the value {choice} is illegal input. please try again")
         print(f"Error: the value {choice} is illegal input. please try again")
         choice="0"
         logger.info("because of unvalid input we put a defultive value to sign the process to continue")
     return choice

def add_shape(shape_manage):
    """
    get new shape name and add it to the shapes list
    :param shape_manage: the shape manger class to handle the add
    :return: None
    """
    shape=input("enter shape").strip().lower()
    if shape.isalpha():
        try:
            is_resembl=False
            for k,v in shape_manage.shapes_dict.items():
                if k == shape:
                    is_resembl = True
                    shape_instance=v
                    new_params=shape_instance().get_params()
            if not is_resembl:
                raise KeyError
            # trying to add a new shape to our collection except of class not found or parameters illegal
            shape_manage.create_shape_1(new_params)
        except KeyError:
            print(f"Error shape class {shape} was not found, please try again")
        except ValueError:
            print("the values of parameters should be positive integers")
    else:
        logger.exception("Error the value should contain only characters ")
        print(f"Error the value {shape} should contain only characters")

def get_shapes(shape_manage):
    """
    print all the shapes details
    :param shape_manage: the shape manger class
    :return:
    """
    logger.info("enter to get_shape function")
    shape_manage.get_all_shapes()

def shape_update(shape_manage):
    """"
    get from the user shape id for update and update the shape parameters
    """
    logger.info("enter to shape_update function")
    try:
        shape_id = int(input("please enter the id shape for update\n"))
        if shape_id <= 0:
            print("Error: shape id must be a positive integer")
            return
    except ValueError:
        print("Error: shape id should be a positive integer")
        logger.exception("Error: shape id should be a positive integer")
        return

    shape_to_update = shape_manage.get_shape_by_id(shape_id)
    if not shape_to_update:
        print(f"Error: the shape id: {shape_id} was not found")
        return

    shape_type = shape_to_update.shape_type
    print(f"The shape of type '{shape_type}' was found")

    try:
        print(f"Please enter the *new* parameters for this {shape_type}:")
        new_data = shape_to_update.get_params()

        shape_manage.update_shape(shape_id, new_data)

        print("The updated list is: \n")
        shape_manage.get_all_shapes()

    except ValueError:
        print("Error: update failed, the parameters must be positive integers")
        return

def delete_shapes(shape_manage):
    """
    get a shape id and delete it from the list
    :param shape_manage: the shape manger class
    :return:
    """
    try:
        shape_id=int(input("please enter shape id to remove").strip())
        if shape_id <= 0:
            print("Error: shape id must be a positive integer")
            return
        shape_manage.delete_shape(shape_id)
    except ValueError:
        logger.exception("Error: the id shape to remove should be a positive integer")
        print("Error: invalid input, shape id must be a positive integer")
        raise

def main():
    processing=True
    while processing:
        choice=show_menu()
        shape_manage=shape_manager.ShapeManager()
        if choice=="0":
            continue
        elif choice=="1":
            try:
                add_shape(shape_manage)
            except KeyError:
                logger.exception(f"Error: the shape you enter is not apart of the shapes of the system")
        elif choice=="2":
            get_shapes(shape_manage)
        if choice=="3":
            try:
                shape_update(shape_manage)
            except ValueError:
                print(f"Error: the paramters you enters is illegal")
            # shape_manager.update_shape(shape_manage)
        elif choice == "4":
            try:
                delete_shapes(shape_manage)
            except ValueError:
                logger.exception("Error: the id shape to remove should be a positive integer")
        elif choice == "5":
            processing=False

if __name__ == '__main__':
    main()