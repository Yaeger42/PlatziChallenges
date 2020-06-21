# VolumeFormula (pi(radius**2)) * height
from math import pi

def cilinderVolume(radius, height):
    return (pi(radius**2)) * height

def main():
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    print(cilinderVolume(radius, height))

if __name__ == '__main__':
    main()