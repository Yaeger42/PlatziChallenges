from math import pi, sqrt

def triangleArea(base, height):
    return (base * height) / 2

def squareArea(side):
    return side**2

def pentagonArea(p, a):
    return (p * a)/2 

def rectangleArea(base, height):
    return base * height

def circleArea(radius):
    return pi * (radius**2)

def menu():
    print("1. Calculate the area of a triangle")
    print("2. Calculate the area of a square")
    print("3. Calculate the area of a pentagon")
    print("4. Calculate the area of a rectangle")
    print("5. Calculate the area of a circle")
    option = int(input("Enter an option with the desired number: "))
    while option <= 5:
        if option == 1:
            base = int(input("Enter the base of the triangle: "))
            height = int(input("Enter the height of the triangle: "))
            print(triangleArea(base, height))

        elif option == 2:
            side = int(input("Enter one size of the square: "))
            print(squareArea(side))
        
        elif option == 3:
            p = float(input("Enter the pentagon's perimeter: "))
            a = float(input("Enter the pentagon's apothem: "))
            print(pentagonArea(p, a))

        elif option == 4:
            b = int(input("Enter the base of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            print(rectangleArea(b, height))

        elif option == 5:
            r = int(input("Enter the radius of the circle: "))
            print(circleArea(r))

        else:
            option = int(input("Enter a valid option: "))

        