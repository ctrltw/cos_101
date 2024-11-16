def physics_and_maths_operations_options():
    print("\nphysics_and_maths_operations_options")
    print("a, area of rectangle  ")
    print("b, work  ")
    print("c,pressure  ")
    print("d, volume of a prism  ")
    print("e, force  ")

physics_and_maths_operations_options()
options =input("pick an option from the options list")
if options == "a":

        breadth = int(input("enter the breadth of the rectangle  "))
        length = int(input("enter the length of the rectangle  "))
        area: int = int(input("enter the area of the rectangle  "))
        area_of_rectangle = breadth * length
        print(area_of_rectangle)

elif options == "b":
        force = int(input("force of the object  "))
        distance= int(input("distance of the object  "))
        work = force * distance
        print(work)

elif options == "c":
        force = int(input("force applied on the object  "))
        area = int(input("area of the force distributed  "))
        pressure = force/area
        print(pressure)

elif options == "d":
        length = int(input("enter the length of the  prism  "))
        width = int(input("enter the width of the prism  "))
        height = int(input("enter the height of the prism  "))
        volume = length * width * height
        print(volume)

elif options == "e":
        mass = int(input("enter the mass of the object  "))
        acceleration = int(input("enter the acceleration of the object  "))
        force = mass * acceleration
        print(force)
else :
    print("option does not exist")











    