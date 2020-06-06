'''
Reto #8 “Divide la cuenta”
Instrucciones: vas con tus amigos a tu restaurante favorito y acuerdan dividir la cuenta. 
Para facilitar las cosa pedirás al usuario que indique el total a pagar, 
entre cuantas personas se dvidirá la cuenta, porcentaje de propina a incluir, 
un porcentaje de impuestos, total a pagar incluyendo propina más impuestos 
y el total a pagar por cada persona.
'''

def billSplit():
    total = int(input("Enter the total: "))
    people = int(input("How many people are there?: "))
    tip = int(input("Enter the percentage of tip you'll include: "))
    taxes = int(input("Enter the percentage of taxes: "))
    totalAndTaxes = float((total * taxes) / 100 + total)
    finalTip = float((total * tip) / 100)
    grandTotal = float(totalAndTaxes + finalTip)
    splittedBill = float(grandTotal / people )
    return print("The total is: " + str(grandTotal) + " and everyone must pay: " + str(splittedBill))

billSplit()
