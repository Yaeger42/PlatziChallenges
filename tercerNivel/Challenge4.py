def formatting (string, fromm, to):

    stringLength = len(string)
    while stringLength > 10:
        if fromm < 0 or to > stringLength:
            print("The length should be greater than 1 but less than the string length")
            return
        formatted = string[fromm:to:]
        return f'Your new formatted string is: {formatted}'

def main():

    #string = input("Enter: ")
    #range1 = int(input("Range 1: "))
    #range2 = int(input("Range 2: "))
    #formation = string[range1:range2:]
    #print(formation)

    string = input("Enter the desired string, it should be greater than 10: \n")
    fromm = int(input("Enter the initial range of the string: "))
    to = int(input("Enter the final range of the string: "))
    print(formatting(string, fromm, to))

if __name__ == '__main__':
    main()
