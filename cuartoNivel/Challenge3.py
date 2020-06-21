from math import sqrt

def squareRoots(n):
    if n < 20:
        return 
    elif n > 20:
        return round(sqrt(n), 3)

def main():
    n1 = float(input("Enter the roor number: "))
    print(squareRoots(n1))

if __name__ == '__main__':
    main()