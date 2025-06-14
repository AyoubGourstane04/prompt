## Exercice 3.1 :

### 1- L'exécution de cette programme : `calculate_average.py`

```python
def calculate_average(numbers_list): 
    # This function calculates the average of numbers in a list 
    # It has some issues 
    total = 0
    for num in numbers_list: 
    total += num 
    average = total / len(numbers_list) 
    return average 

# Example of usage (might cause errors) 
my_nums = [1, 2, 'three', 4] # <-- Error here 
avg = calculate_average(my_nums) 
print(f"Average: {avg}")
```

**Donne l'erreur suivant :**

```
Traceback (most recent call last):
  File "c:\Users\hp\Desktop\prompt\ex3\ex3.1\test.py", line 12, in <module>
    avg = calculate_average(my_nums)
  File "c:\Users\hp\Desktop\prompt\ex3\ex3.1\test.py", line 6, in calculate_average
    total += num
TypeError: unsupported operand type(s) for +=: 'int' and 'str
```

### 2- Prompt :
> " Le code suivant vise à calculer la moyenne d’une liste de nombres, mais il contient une erreur. Analysez le code, identifiez précisément l’erreur qui provoque une exception lors de l’exécution, puis proposez une version corrigée du code qui gère ce type d’erreur de manière appropriée.
>
> ```python
> def calculate_average(numbers_list): 
>     # This function calculates the average of numbers in a list 
>     # It has some issues 
>     total = 0
>     for num in numbers_list: 
>     total += num 
>     average = total / len(numbers_list) 
>     return average 
>
> # Example of usage (might cause errors) 
> my_nums = [1, 2, 'three', 4] # <-- Error here 
> avg = calculate_average(my_nums) 
> print(f"Average: {avg}")
> ```
>
> Lors de l'exécution, le message d'erreur est :
>
> ```
> Traceback (most recent call last): File "c:\Users\hp\Desktop\prompt\ex3\ex3.1\test.py", line 12, in <module> avg = calculate_average(my_nums) File "c:\Users\hp\Desktop\prompt\ex3\ex3.1\test.py", line 6, in calculate_average total += num TypeError: unsupported operand type(s) for +=: 'int' and 'str
> ```
> "

**Resultat :** `calculate_averageCorr.py`

L’erreur dans votre code est due à la présence d’une chaîne de caractères ('three') dans la liste my_nums. Python ne peut pas additionner un entier (int) avec une chaîne (str), ce qui déclenche une exception TypeError.

**Correction du code :**

Une solution consiste à filtrer les valeurs non numériques ou à lever une exception avec un message explicite.

```python
def calculate_average(numbers_list):
    """Calculate the average of a list of numbers, handling invalid inputs."""
    total = 0
    valid_count = 0
    
    for num in numbers_list:
        if isinstance(num, (int, float)):  # Vérification du type numérique
            total += num
            valid_count += 1
        else:
            print(f"Avertissement : '{num}' ignoré (non numérique)")
    
    if valid_count == 0:
        raise ValueError("La liste ne contient aucun nombre valide.")
    
    return total / valid_count

# Exemple d'utilisation
my_nums = [1, 2, 'three', 4] 
avg = calculate_average(my_nums)
print(f"Moyenne : {avg}")
```

**Améliorations apportées :**

*   Vérification du type : Seuls les nombres (int et float) sont pris en compte.
*   Ignorer avec un message : Les éléments non numériques sont signalés mais ne provoquent pas une erreur bloquante.
*   Gestion des cas extrêmes : Si aucun élément valide n'est trouvé, une exception ValueError est levée.

### 3- Prompt :
> "générer des tests unitaires avec pytest pour valider son comportement."

**Resultat :** `test_calculate_average.py`

```python
import pytest
from calculate_averageCorr import calculate_average  # Remplacez 'your_module' par le nom réel de votre module

def test_average_with_valid_numbers():
    """Test avec une liste de nombres valides."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_average_with_mixed_types():
    """Test avec des types mixtes où les non-numériques doivent être ignorés."""
    assert calculate_average([1, 2, 'three', 4, 5]) == 3.0  # 'three' ignoré

def test_average_with_only_non_numeric():
    """Test avec une liste ne contenant que des valeurs non numériques, déclenchant une exception."""
    with pytest.raises(ValueError, match="La liste ne contient aucun nombre valide."):
        calculate_average(['one', 'two', 'three'])

def test_average_with_empty_list():
    """Test avec une liste vide, qui devrait lever une exception."""
    with pytest.raises(ValueError, match="La liste ne contient aucun nombre valide."):
        calculate_average([])

def test_average_with_floats():
    """Test avec des nombres flottants pour vérifier la précision."""
    assert calculate_average([1.5, 2.5, 3.0]) == 2.3333333333333335  # Vérification des décimales
```