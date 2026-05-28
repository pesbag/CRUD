from logging import exception

import shape_manager
import logging

logger=logging.getLogger('shape')

def show_menu():
     choice=input("press 1 to Add shape\n "
          "press 2 to Show all shapes\n "
          "press 3 to Update shape\n "
          "press 4 to Delete shape\n "
          "press 5 to Exit ")
     is_valid=validate_chose_menu(choice)
     logger.info("check the validation of the user input")
     if not is_valid:
         choice="0"
     return choice

def validate_chose_menu(choice):
    """
    check the validation of  the choice which include only digits
    :return: True if valid, else False
    """
    for c in choice:
        if not c.isdigit:
            return False
    return True

def add_shape(shape_manage):
    """
    get new shape name and add it to the shapes list
    :param shape_manage: the shape manger class to handle the add
    :return: None
    """
    shape=input("enter shape")
    is_valid_shape=validate_shape_input(shape)
    if is_valid_shape:
        shape_manage.create_shape(shape)
    else:
        logger.exception("Error the value should contain only characters ")

def validate_shape_input(shape):
    """
    get a shape object name and check if it valid name
    return True if valid. False else
    """
    for c in shape:
        if not c.isalpha:
            return True
    return False

def get_shapes(shape_manage):
    """
    print all the shapes details
    :param shape_manage: the shape manger class
    :return:
    """
    shape_manage.get_all_shapes()

# def update_shape(shape_manage):
#     shape_manage.

def delete_shapes(shape_manage):
    """
    get a shape id and delete it from the list
    :param shape_manage: the shape manger class
    :return:
    """
    try:
        shape_id=int(input("please enter shape id to remove"))
        shape_manage.delete_shape(shape_id)
    except ValueError:
        logger.exception("Error: the id shape to remove should be a positive integer")
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
                logger.exception(f"Error: the shape you enterd is not apart of the shapes of the system")
        elif choice=="2":
            get_shapes(shape_manage)
        # if choice=="3":
        #     shape_manager.update_shape()
        elif choice == "4":
            try:
                delete_shapes(shape_manage)
            except ValueError:
                logger.exception("Error: the id shape to remove should be a positive integer")
        elif choice == "5":
            processing=False

if __name__ == '__main__':
    main()