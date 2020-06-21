def food(name, lastName, favouriteFood):
    x = f"Hello, my name is {name} {lastName} and my favourite food is {favouriteFood}"
    return x


def main():
    name = input("Enter your name: ")
    lastName = input("Enter your last name: ")
    favouriteFood = input("Enter your favourite food: ")

    print(food(name, lastName, favouriteFood))


if __name__ == '__main__':
    main()