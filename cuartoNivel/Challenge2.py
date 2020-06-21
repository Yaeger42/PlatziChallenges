def multiplyDecimals(n1, n2):

    result = round(n1*n2, 4)
    return result

def main():
    n1 = float(input("Enter the first number with decimals: "))
    n2 = float(input("Enter the second number with decimals: "))
    print(multiplyDecimals(n1, n2))

if __name__ == '__main__':
    main()
