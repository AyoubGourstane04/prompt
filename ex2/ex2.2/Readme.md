## Exercice 2.2

### Prompt1 : `prompt1.py`

* **Prompt basé sur la Règle (zéro-Shot Prompting)** :
  Crée une fonction Python format\_product\_code(product\_id). Le product\_id doit être une chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le 7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères non alphanumériques, elle doit lever une ValueError. Inclue un docstring.

* **Résultat** :

```python
def format_product_code(product_id: str) -> str:
    """
    Formate un identifiant de produit en insérant des tirets.

    Args:
        product_id (str): Chaîne de 10 caractères alphanumériques.

    Returns:
        str: Identifiant formaté avec des tirets.

    Raises:
        ValueError: Si l'identifiant ne fait pas 10 caractères ou contient des caractères non alphanumériques.
    """
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
```

* **Réponse Au Question** :
  Le code est correct grâce aux points suivants :

  * Validation rigoureuse : Il s’assure que `product_id` est une chaîne alphanumérique de 10 caractères avant de la formater, empêchant les entrées invalides.
  * Gestion des erreurs efficace : Une `ValueError` est levée avec un message explicite lorsque l’entrée ne respecte pas les contraintes, évitant ainsi des comportements imprévus.
  * Lisibilité et respect des normes : Le code est clair, bien structuré et conforme aux standards PEP8, ce qui améliore sa maintenabilité.

  Cependant, la gestion des erreurs peut être améliorée, car certaines exceptions potentielles ne sont pas prises en compte. Une validation supplémentaire pourrait renforcer sa robustesse.

---

### Prompt2 : `prompt2.py`

* **Prompt avec un Exemple (One-Shot Prompting)** :
  "Crée une fonction Python format\_product\_code(product\_id). Le product\_id doit être une chaîne de 10 caractères  alphanumériques. Voici un exemple d'entrée-sortie: format\_product\_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit lever une ValueError si l'entrée est invalide. Inclue un docstring".

* **Résultat** :

```python
def format_product_code(product_id: str) -> str:
    """
    Formate un identifiant de produit en insérant des tirets.

    Exemple :
        format_product_code("ABC123DEF4") -> "ABC-123-DEF4"

    Args:
        product_id (str): Chaîne de 10 caractères alphanumériques.

    Returns:
        str: Identifiant formaté avec des tirets.

    Raises:
        ValueError: Si l'identifiant ne fait pas 10 caractères ou contient des caractères non alphanumériques.
    """
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
```

* **Réponse Au Question** :
  Oui, l'exemple fourni a clairement facilité la tâche pour générer la bonne fonction. Dans la première réponse, un tiret avait été inséré après le troisième et le septième caractère, conformément à l'interprétation initiale de la demande. Cependant, l'exemple donné a permis une meilleure compréhension de la structure souhaitée, ce qui a conduit à une correction de la segmentation, plaçant les tirets après le 3ᵉ et le 6ᵉ caractère au lieu du 7ᵉ.

  Cet ajustement démontre qu'un exemple bien choisi peut aider à clarifier les attentes et à éviter des erreurs d'interprétation. Il s'agit d'un excellent moyen de guider une IA vers une réponse plus précise. Si des variantes doivent être testées ou si des améliorations supplémentaires sont souhaitées pour la fonction, il est toujours possible d'apporter des ajustements.

---

### Prompt3 : `prompt3.py`

* **Prompt avec Multiple Exemples (Few-Shot prompting)** :
  Reprenez le prompt précédent et ajoutez un deuxième exemple d'entrée-sortie: format\_product\_code("XYZ987GHIJ") devrait retourner "XYZ-987-GHIJ", incluant un cas d'erreur : format\_product\_code("SHORT") devrait lever une ValueError.

* **Résultat** :

```python
def format_product_code(product_id: str) -> str:
    """
    Formate un identifiant de produit en insérant des tirets.

    Exemples :
        format_product_code("ABC123DEF4") -> "ABC-123-DEF4"
        format_product_code("XYZ987GHIJ") -> "XYZ-987-GHIJ"

    Args:
        product_id (str): Chaîne de 10 caractères alphanumériques.

    Returns:
        str: Identifiant formaté avec des tirets.

    Raises:
        ValueError: Si l'identifiant ne fait pas 10 caractères ou contient des caractères non alphanumériques.

    Exemple d'erreur :
        format_product_code("SHORT")  # Lève une ValueError
    """
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
```

* **Réponse Au Question** :
  Oui, la gestion des erreurs est désormais plus robuste grâce à l'ajout d'un exemple explicite. Toute entrée invalide est immédiatement détectée, garantissant un comportement fiable. On peut encore affiner le message d'erreur ou ajouter des tests unitaires si nécessaire.

---

### Tests par pytest :

```python
import pytest
from prompt1 import format_product_code as format_product_code_prompt1
from prompt2 import format_product_code as format_product_code_prompt2
from prompt3 import format_product_code as format_product_code_prompt3

# Tests pour prompt1
def test_valid_product_code_prompt1():
    result = format_product_code_prompt1("ABC1234XYZ")
    print(f"Test prompt1 valide: {result}")
    assert result == "ABC-1234-XYZ"

def test_invalid_length_prompt1():
    with pytest.raises(ValueError, match="Le product_id doit être une chaîne de 10 caractères alphanumériques."):
        print("Test prompt1 erreur longueur: devrait lever une ValueError")
        format_product_code_prompt1("SHORT")

def test_invalid_characters_prompt1():
    with pytest.raises(ValueError):
        print("Test prompt1 erreur caractères invalides: devrait lever une ValueError")
        format_product_code_prompt1("ABC!23@XYZ")

# Tests pour prompt2
def test_valid_product_code_prompt2():
    result1 = format_product_code_prompt2("ABC123DEF4")
    result2 = format_product_code_prompt2("XYZ987GHIJ")
    print(f"Test prompt2 valide: {result1}, {result2}")
    assert result1 == "ABC-123-DEF4"
    assert result2 == "XYZ-987-GHIJ"

def test_invalid_length_prompt2():
    with pytest.raises(ValueError, match="Le product_id doit être une chaîne de 10 caractères alphanumériques."):
        print("Test prompt2 erreur longueur: devrait lever une ValueError")
        format_product_code_prompt2("SHORT")

def test_invalid_characters_prompt2():
    with pytest.raises(ValueError):
        print("Test prompt2 erreur caractères invalides: devrait lever une ValueError")
        format_product_code_prompt2("XYZ@87GHIJ")

# Tests pour prompt3 (identique à prompt2 mais regroupé ici)
def test_valid_product_code_prompt3():
    result1 = format_product_code_prompt3("ABC123DEF4")
    result2 = format_product_code_prompt3("XYZ987GHIJ")
    print(f"Test prompt3 valide: {result1}, {result2}")
    assert result1 == "ABC-123-DEF4"
    assert result2 == "XYZ-987-GHIJ"

def test_invalid_length_prompt3():
    with pytest.raises(ValueError, match="Le product_id doit être une chaîne de 10 caractères alphanumériques."):
        print("Test prompt3 erreur longueur: devrait lever une ValueError")
        format_product_code_prompt3("SHORT")

def test_invalid_characters_prompt3():
    with pytest.raises(ValueError):
        print("Test prompt3 erreur caractères invalides: devrait lever une ValueError")
        format_product_code_prompt3("XYZ@87GHIJ")
```

---

## Analyse Critique

### 1. L’ajout d’exemples a grandement affiné la compréhension des consignes par l’IA, surtout pour les règles complexes :

* Clarification des attentes : Les exemples définissent précisément le comportement attendu, réduisant les erreurs d’interprétation.
* Robustesse améliorée : La gestion des exceptions est plus efficace grâce à l’inclusion de cas d’erreur dans le prompt.
* Précision accrue : Les exemples orientent l’IA vers une structure de code exacte, minimisant les approximations.
* Adaptabilité renforcée : L’IA ajuste ses réponses aux formats attendus avec plus de cohérence.

Ce procédé optimise la fiabilité du code généré et améliore la pertinence des résultats.

---

### 2. Le "Few-Shot Prompting" est particulièrement utile en développement lorsqu'il faut gérer :

* Des cas complexes d'entrée et de sortie, où plusieurs exemples sont nécessaires pour guider l'IA vers un format précis.

* Des règles complexes de gestion d'erreurs, permettant de mieux anticiper les exceptions et valider les entrées correctement.

---

### 3. Les limites des exemples

Le "Few-Shot Prompting" présente certaines limites, notamment :

* Couverture incomplète : Certains cas peuvent être bien illustrés tandis que d'autres sont ignorés, ce qui peut entraîner des erreurs ou des biais dans la réponse.
* Qualité des exemples : Un exemple mal rédigé ou peu clair peut compliquer la compréhension du problème par l'IA et produire des résultats incorrects.
* Nombre d'exemples : Trop peu d'exemples laissent l'IA dans l'incertitude, tandis qu'un excès peut nuire à l'efficacité et ralentir le traitement. Trouver un équilibre est essentiel pour guider l'IA sans surcharge cognitive.
