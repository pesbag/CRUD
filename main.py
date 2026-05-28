import shape_manager
def show_menu():
     choice=input(print("press 1 to Add shape\n "
          "press 2 to Show all shapes\n "
          "press 3 to Update shape\n "
          "press 4 to Delete shape\n "
          "press 5 to Exit "))
     return choice

def add_shape(shape_manage):
    shape=input("enter shape")
    shape_manage.create_shape(shape)

def get_shapes(shape_manage):
    shape_manage.get_all_shapes()

# def update_shape(shape_manage):
#     shape_manage.

def delete_shapes(shape_manage):
    try:
        shape_id=int(input("please enter shape id to remove"))
        shape_manage.delete_shape(shape_id)
    except ValueError:
        return "Error: the id shape to remove should be a positive integer"


def main():
    processing=True
    while processing:
        choice=show_menu()
        shape_manage=shape_manager.ShapeManager()
        if choice=="1":
            add_shape(shape_manage)
        if choice=="2":
            get_shapes(shape_manage)
        # if choice=="3":
        #     shape_manager.update_shape()
        if choice == "4":
            delete_shapes(shape_manage)
        if choice == "5":
            processing=False

if __name__ == '__main__':
    main()