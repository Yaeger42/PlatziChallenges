def raining(itsRaning):

    x = itsRaning.lower()
    if x == 'yes':
        itsWindy = input("Is it windy?: ")
        y = itsWindy.lower()
        if y == 'yes':
            return print("Maybe it's too windy to take an umbrella")
        elif y == 'no':
            return print("You should take an umbrella with you")
    elif itsRaning ==  'no' :
        return print("Have a nice day")    
    

def main():
    rain = input("Is it raining?: ")
    raining(rain)


if __name__ == '__main__':
    main()