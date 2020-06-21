def pigLatin(string):
    
    if string.startswith("a") or string.startswith("e") or string.startswith("i") or string.startswith("o") or string.startswith("u"):
        return f"{string.capitalize()}way"
    else:
        start = string[0:1:].lower()
        newString = string[1::] + start + "ay"
        return f"{newString.capitalize()}"



def main():
    string = input("Enter a word: ")
    print(pigLatin(string))

if __name__ == '__main__':
    main()