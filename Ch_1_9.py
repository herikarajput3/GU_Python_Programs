choice = 0
while(choice !=5):
    print()
    print("1. Find area of circle")
    print("2. Find area of triangle")
    print("3. Area of square and rectangle")
    print("4. Find simple interest")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        PI = 3.14
        radius = float(input("Please enter the radius of a circle:"))
        area = PI * radius * radius
        print("Area of a circle = %.2f" %area)

    elif choice == 2:
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))
        # calculate the semi-perimeter
        s = (a+b+c)/2
            # calculate the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of the triangle is %0.2f" %area)

    elif choice==3:
        side = int(input("Enter side length of square:"))
        area_square = side * side
        print("Area of square = ",area_square)
        width = float(input("Please enter the width of a rectangle: "))
        height = float(input("Please enter the height of a rectangle: "))
            # calculate the area
        Area = width * height
        print("\n Area of rectangle is: %.2f" %Area)

    elif choice==4:
        p = int(input("Enter P: "))
        r = int(input("Enter R: "))
        n = int(input("Enter N: "))
        i = (p*r*n)/100
        print(i)
        
    elif choice==5:
        exit()
        
    else:
        print("Bye Bye")
