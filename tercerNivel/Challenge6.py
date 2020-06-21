def shortAndLong(name):

    if len(name) > 5:
        return f"Hello {name.capitalize()}"
    
    elif len(name) < 5:
        lastName = input("Please enter your last name: ")
        return f"Hello {name.capitalize()} {lastName.capitalize()}"


def main():
    name = input("Enter your name: ")
    print(shortAndLong(name))

if __name__ == '__main__':
    main()    