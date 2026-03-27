op1 = int(input("Entrez le premier opérande : "))
opr = input("Entrez l'opérateur. Les symboles acceptés sont +, -, *, /, //, ** : ")
op2 = int(input("Entrez le deuxième opérande : "))

def calcul(op1, opr, op2):
    if opr == "+":
        res = op1 + op2
    elif opr == "-":
        res = op1 - op2
    elif opr == "*":
        res = op1 * op2
    elif opr == "/":
        if op2 != 0:
            res = op1 / op2
        else:
            res = "Impossible de diviser par zéro."
    elif opr == "//":
        if op2 != 0:
            res = op1 // op2
        else:
            res = "Impossible de diviser par zéro."
    elif opr == "**":
        res = op1 ** op2
    else:
        res = "Opérateur non reconnu."
    return res

print(calcul(op1, opr, op2))