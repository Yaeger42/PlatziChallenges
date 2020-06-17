def mAndM(n, m ):

    if m > n:
        result = m - n
        return print(f'{m} is greater than {n} and the difference between th two is: {result}')

    elif m == n:
        return print("Both terms are equal")

    elif m < n:
        result = n - m
        return print(f"{n} is greater than {m} and the difference between the two is: {result}")



def main():
    m = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    mAndM(n, m)

if __name__ == '__main__':
    main()