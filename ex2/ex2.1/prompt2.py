def calculate(a: int, b: int, op: str) -> float:
    """
    Effectue une opération mathématique entre deux entiers.

    Paramètres:
    a (int): Premier entier.
    b (int): Deuxième entier.
    op (str): Opération à effectuer ('+', '-', '*', '/').

    Retourne:
    float: Résultat de l'opération arrondi à deux décimales.
           Retourne un message d'erreur en cas d'opération invalide.
    """
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "Erreur: division par zéro"
            return round(a / b, 2)
        else:
            return "Erreur: opération invalide"
    except Exception as e:
        return f"Une erreur est survenue: {e}"
