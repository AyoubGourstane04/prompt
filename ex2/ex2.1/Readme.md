## Exercice 2.1

### Prompt1 : `prompt1.py`

* **Prompt Vague** :
  "Écris une fonction pour faire des opérations entre deux nombres en Python."

* **Résultat** :

```python
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
```

* **Réponse Au Question** :
  La fonction est nommée et tous les  opérations de base sont prises en charge , la gestion des erreurs est effectué dans le cas de division par zéro et le cas d’opération invalide, et il n’offre pas des commentaires dans le corps du fonction et ne conforme pas au prototype de fonction donné au question au-dessus.

---

### Prompt2 : `prompt2.py`

* **Prompt Spécifique** :
  "Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une chaîne op indiquant '+', '-', '\*', ou '/'. La fonction doit retourner le résultat de l’opération, gérer les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux décimales. Ajoute un docstring détaillé et des commentaires."

* **Résultat** :

```python
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
```

* **Réponse Au Question** :
  La fonction (calculate) ci-dessus est nettement supérieure au celui de question précédent car elle est plus robuste grâce à son bloc try...except qui gère toutes les erreurs sans planter. Elle est aussi plus lisible en utilisant des opérateurs standards (+, -) et des conventions modernes comme les "type hints". Enfin, elle est plus complète car elle couvre plus de cas d'erreur et effectue l'arrondi pour la division.

---

### Prompt3 : `prompt3.py`

* **Prompt avec Persona** :
  "En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '\*', '/'). La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des commentaires clairs."

* **Résultat** :

```python
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
```

* **Réponse Au Question** :
  Cette version est plus professionnelle grâce à son respect des conventions PEP8 et sa clarté. Elle est mieux structurée, utilisant un dictionnaire pour simplifier la logique et améliorer la lisibilité. Enfin, elle est plus sécurisée, avec une validation stricte des entrées et une gestion robuste des erreurs.

---

### Tests par pytest :

```python
import pytest
from prompt1 import calculate as calculate_1
from prompt2 import calculate as calculate_2
from prompt3 import calculate as calculate_3

def test_addition():
    """Test de l'addition."""
    result_1 = calculate_1(10, 5, "addition")
    result_2 = calculate_2(10, 5, "+")
    result_3 = calculate_3(10, 5, "+")
    
    assert result_1 == 15
    assert result_2 == 15
    assert result_3 == 15

def test_soustraction():
    """Test de la soustraction."""
    result_1 = calculate_1(10, 5, "soustraction")
    result_2 = calculate_2(10, 5, "-")
    result_3 = calculate_3(10, 5, "-")
    
    assert result_1 == 5
    assert result_2 == 5
    assert result_3 == 5

def test_multiplication():
    """Test de la multiplication."""
    result_1 = calculate_1(10, 5, "multiplication")
    result_2 = calculate_2(10, 5, "*")
    result_3 = calculate_3(10, 5, "*")
    
    assert result_1 == 50
    assert result_2 == 50
    assert result_3 == 50

def test_division():
    """Test de la division et de l'arrondi."""
    result_1 = calculate_1(10, 3, "division")
    result_2 = calculate_2(10, 3, "/")
    result_3 = calculate_3(10, 3, "/")
    
    assert result_1 == 3.3333333333333335
    assert result_2 == 3.33
    assert result_3 == 3.33

def test_division_par_zero():
    """Test de la gestion de la division par zéro."""
    result_1 = calculate_1(10, 0, "division")
    result_2 = calculate_2(10, 0, "/")
    result_3 = calculate_3(10, 0, "/")
    
    assert result_1 == "Erreur: division par zéro"
    assert result_2 == "Erreur: division par zéro"
    assert result_3 == "Erreur: division par zéro"

def test_operateur_invalide():
    """Test de la gestion des opérateurs invalides."""
    result_1 = calculate_1(10, 5, "%")
    result_2 = calculate_2(10, 5, "%")
    result_3 = calculate_3(10, 5, "%")
    
    assert result_1 == "Opération non reconnue"
    assert result_2 == "Erreur: opération invalide"
    assert result_3 == "Erreur: opérateur invalide"
```

---

## Analyse Critique

### 1. Les différences entre les trois implémentations de `calculate()` résident principalement dans la gestion des erreurs, la structuration et la clarté :

1. `prompt1.py` (Basique) : Implémentation simple avec une logique conditionnelle `if-elif`. Absence de gestion avancée des erreurs et de validation des entrées.
2. `prompt2.py` (Améliorée) : Ajoute une **gestion des exceptions** et un **arrondi pour la division**, améliorant la robustesse du code.
3. `prompt3.py` (Optimisée) : Respecte **strictement PEP8**, utilise un **dictionnaire** pour améliorer la lisibilité, inclut une **validation des types** et gère **toutes les erreurs** de façon claire et détaillée.

La troisième version est **plus professionnelle**, **mieux structurée**, et **plus sécurisée**.

---

### 2. Le principe de Prompt Engineering qui a eu le plus grand impact sur le résultat :

Le persona a eu le plus grand impact, car il définit le ton et le niveau d'expertise attendu dans la réponse. En précisant "En tant que développeur Python", le prompt oriente la solution vers une implémentation professionnelle, bien structurée et conforme aux bonnes pratiques. Cependant, la spécificité joue aussi un rôle clé en détaillant les exigences techniques (gestion des erreurs, arrondi des divisions, PEP8), garantissant une réponse robuste et directement applicable.

---

### 3. L'IA a-t-elle introduit des erreurs ou des comportements inattendus dans une des versions ?

Non, toutes les versions fonctionnent correctement sans erreurs majeures. Cependant, certaines implémentations offrent une meilleure robustesse et gestion des erreurs, rendant le code plus fiable et maintenable.

---

### 4. Le coût pour obtenir un code de haute qualité :

**Un prompt vague** entraîne un code plus basique, nécessitant plus de temps et d’effort pour le rendre robuste, avec plusieurs itérations et corrections. En revanche, **un prompt spécifique** guide immédiatement l’IA vers un code bien structuré, sécurisé et conforme aux bonnes pratiques, réduisant ainsi le besoin d’améliorations.
