def capitalization(word1, word2):

    x = word1.upper()
    x2 = word2.upper()
    return f"{x}\n{x2}"

def main():
    string1 = input("Enter the first word: ")
    string2 = input("Enter the second word: ")
    print(capitalization(string1, string2))

if __name__ == '__main__':
    main()