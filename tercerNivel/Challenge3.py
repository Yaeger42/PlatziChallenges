def caps(name, lastName, coo):
    
    n = name.capitalize()
    l = lastName.capitalize()
    coo = coo.capitalize()

    return f"{n}\n{l}\n{coo}"


def main():
    name = input("Enter your name: ")
    lastName = input("Enter your last name: ")
    coo = input("Enter your country of origin: ")

    print(caps(name, lastName, coo))


if __name__ == '__main__':
    main()