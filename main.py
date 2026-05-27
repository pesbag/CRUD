import shape_manager
def show_menu():
     choice=input(print("press 1 to Add shape\n"
          "press 2 to Show all shapes\n"
          "press 3 to Update shape\n"
          "press 4 to Delete shape\n"
          "press 5 to Exit"))
     return choice
def add_shape(shape_manage):
    shape=input("enter shape")
    new_shape = shape_manage.create_shape(shape)

def main():
    choice=show_menu()
    shape_manage=shape_manager.ShapeManager()
    if choice=="1":
        add_shape()
    if choice=="2":
        shape_manager.get_all_shapes(self)
    if choice=="3":
        shape_manager.
    if choice == "4":

    if choice == "5":
        exit()

if __name__ == '__main__':
    main()