def ranges2(x, y, z):

    if z <= y or z <= x:
        return print(f'{z} is within the limits')
    
    elif z > x or z < y:
        return print(f'{z} is out of bounds')


def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = int(input("Enter the third number: "))
    ranges2(x, y, z)


if __name__ == '__main__':
    main()