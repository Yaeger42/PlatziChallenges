def integersAndResidues(n1, n2):
    resultWithoutResidue = n1 // n2
    residue = n1 % n2
    return f'{n1} divided {n2} is {resultWithoutResidue} and the residue is {residue}'



def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(integersAndResidues(9, 2))

if __name__ == '__main__':
    main()