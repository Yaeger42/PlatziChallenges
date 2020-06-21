from math import sqrt, pi 

def circle(radius):
    return pi * (radius**2)

def main():
    radius = float(input("Enter the circle radius: "))
    print(circle(radius))

if __name__ == '__main__':
    main()