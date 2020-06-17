def turtles(turtle):
    
    turtleL = ['tortuga', 'Tortuga', 'TORTUGA']
    if turtle in turtleL:
        return print("I like turtles too")
    else:
        return print("That's a cool animal but I prefer turtles")

def main():
    turts = input("What's your favourite animal?: ")
    turtles(turts)


if __name__ == '__main__':
    main()