op1 = int(input("Entrez le premier opérande : "))
opr = str(input("Entrez l'opérateur. Les symboles acceptés sont +, -, *, /, //, ** : "))
op2 = int(input("Entrez le deuxième opérande : "))
res = None

def calcul(op1, opr, op2) -> res:
    if opr == "+":
        res = op1 + op2

    if opr == "-":
        res = op1 - op2

    if opr == "*":
        res = op1 * op2

    if opr == "/":
        if op2 != 0:
            res = op1 / op2
    else:
        res = "Impossible de diviser par zéro."
    
    if opr == "//":
        if op2 != 0:
            res = op1 // op2
        else:
            res = "Impossible de diviser par zéro."
    
    if opr == "**":
        res = op1**op2
    
    return res