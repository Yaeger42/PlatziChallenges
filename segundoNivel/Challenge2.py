def ranges(x, y):

    if y > x:
        return print(f"The number {y} exceeds the bounds")

    elif y < x:
        return print(f"The number {y} is within the bounds")


def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    ranges(x, y)

if __name__ == '__main__':
    main()