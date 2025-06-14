def calculate(a, b, operation):
    if operation == "addition":
        return a + b
    elif operation == "soustraction":
        return a - b
    elif operation == "multiplication":
        return a * b
    elif operation == "division":
        return a / b if b != 0 else "Erreur: division par zéro"
    else:
        return "Opération non reconnue"
