def answers(number):

    da = {
        1 : "Hoy aprenderemos sobre prorgamación",
        2 : "¿Qué tal tomar un curso de marketing digital?",
        3 : "Hoy es un gran día para comenzar a aprender de diseño",
        4 : "¿Y si aprendemos algo de negocios online?",
        5 : "Veamos un par de clases sobre producción audiovisual",
        6 : "Tal vez sea bueno desarrollar una habilidad blanda en Platzi",
    }
    while number not in da:
        number = int(input("Please enter a valid value: "))
    if number in da:
        return print(da.get(number))

    
def main():
    n = int(input("Enter an option in the range of 1 to 6: "))
    answers(n)

if __name__ == '__main__':
    main()