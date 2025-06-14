def calculate(a: int, b: int, op: str) -> float:
    """
    Effectue une opération mathématique entre deux entiers avec une gestion stricte des erreurs.

    Paramètres:
        a (int): Premier entier.
        b (int): Deuxième entier.
        op (str): Opération mathématique ('+', '-', '*', '/').

    Retourne:
        float: Résultat arrondi à deux décimales.
        str: Message d'erreur si l'opération est invalide ou si division par zéro.

    Exemples:
        >>> calculate(10, 5, "+")
        15
        >>> calculate(10, 0, "/")
        'Erreur: division par zéro'
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return "Erreur: les paramètres doivent être des entiers"

    try:
        operations = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": round(a / b, 2) if b != 0 else "Erreur: division par zéro"
        }
        return operations.get(op, "Erreur: opérateur invalide")
    except Exception as e:
        return f"Une erreur est survenue: {e}"
