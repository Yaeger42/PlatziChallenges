def allowed(age):
    if age > 30:
        return print("It's never too late to learn, what course are you taking today?")
    elif age >= 18 and age <= 29:
        return print("This is an excelent moment to push your career")
    elif age < 18:
        return print("Do you know where you'll head your future at? I can surely help you")

def main():
    age = input("Please enter your age: ")
    allowed(age)


if __name__ == '__main__':
    main()