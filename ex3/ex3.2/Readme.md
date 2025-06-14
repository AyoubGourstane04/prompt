## Exercice 3.2 :

**code de départ :** `fct.py`

```python
a = [5, 3, 8, 6, 7, 2] 
for i in range(len(a)): 
    for j in range(i+1, len(a)): 
        if a[i] > a[j]: 
            tmp = a[i] 
            a[i] = a[j] 
            a[j] = tmp 
print(a)
```

### 1- Analyser de code :

*   Ce code trie un tableau en ordre croissant en utilisant un algorithme qui ressemble à l’algorithme de tri par sélection.
*   Les défauts de lisibilité sont les suivants :
    *   Les variables ne sont pas nommées de manière sémantique (par exemple `i`, `j`, `tmp`).
    *   L'absence de commentaires rend le code plus difficile à comprendre, surtout pour quelqu’un qui ne connaît pas son fonctionnement.

### 2- Prompt de refactoring :

> "Le code suivant trie un tableau en ordre croissant à l’aide d’un algorithme proche du tri par sélection. Cependant, il présente des problèmes de lisibilité (noms de variables peu explicites, absence de commentaires, structure peu claire). Refactorez ce code pour le rendre plus lisible et compréhensible.
>
> Objectifs :
>
> Renommer les variables avec des noms explicites.
>
> Ajouter des commentaires clairs pour expliquer chaque étape.
>
> Améliorer la structure générale du code si nécessaire (par exemple : extraire en fonction nommée).
>
> Code :
>
> ```python
> a = [5, 3, 8, 6, 7, 2] 
> for i in range(len(a)): 
>     for j in range(i+1, len(a)): 
>         if a[i] > a[j]: 
>             tmp = a[i] 
>             a[i] = a[j] 
>             a[j] = tmp 
> print(a)
> ```
> "

**Résultat :** `fctCorr1.py`

```python
def selection_sort(arr):
    """ Trie un tableau en ordre croissant en utilisant un algorithme similaire au tri par sélection. """
    for current_index in range(len(arr)):
        for next_index in range(current_index + 1, len(arr)):
            # Échange les éléments si celui à l'index courant est plus grand que le suivant
            if arr[current_index] > arr[next_index]:
                arr[current_index], arr[next_index] = arr[next_index], arr[current_index]
    
    return arr

# Exemple d'utilisation
numbers = [5, 3, 8, 6, 7, 2]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
```

**Améliorations :**

*   Noms explicites : arr, current_index, et next_index rendent le code plus compréhensible.
*   Commentaires : Ajout d'explications pour faciliter la lecture.
*   Structure améliorée : Le tri est encapsulé dans une fonction selection_sort, ce qui améliore la réutilisabilité et la lisibilité du code.
*   Échange direct des valeurs : Utilisation de l'assignation multiple `arr[current_index], arr[next_index] = arr[next_index], arr[current_index]` au lieu d'une variable temporaire.

### 3- Ajout des contraintes :

**Prompt :**

> "Le code suivant trie un tableau en ordre croissant à l’aide d’un algorithme proche du tri par sélection. Cependant, il présente des problèmes de lisibilité (noms de variables peu explicites, absence de commentaires, structure peu claire).Refactorez ce code en respectant les contraintes suivantes :
>
> *   Respecter la convention **PEP8** (indentation, espaces, noms de variables, etc.).
> *   Ajouter des **docstrings** pour documenter les fonctions.
> *   Séparer le code en **fonctions modulaires**.
> *   Utiliser des **noms explicites** pour les variables et les fonctions.
> *   Ajouter un bloc d’exécution : `if __name__ == "__main__":`
>
> Code :
>
> ```python
> a = [5, 3, 8, 6, 7, 2] 
> for i in range(len(a)): 
>     for j in range(i+1, len(a)): 
>         if a[i] > a[j]: 
>             tmp = a[i] 
>             a[i] = a[j] 
>             a[j] = tmp 
> print(a)
> ```
> "

**Résultat :** `fctCorr2.py`

```python
def swap_elements(arr, index1, index2):
    """
    Échange deux éléments dans un tableau.

    Args:
        arr (list): Liste contenant les éléments.
        index1 (int): Index du premier élément.
        index2 (int): Index du deuxième élément.
    """
    arr[index1], arr[index2] = arr[index2], arr[index1]


def selection_sort(arr):
    """
    Trie un tableau en ordre croissant en utilisant un algorithme similaire au tri par sélection.

    Args:
        arr (list): Liste des éléments à trier.

    Returns:
        list: Liste triée en ordre croissant.
    """
    for current_index in range(len(arr)):
        for next_index in range(current_index + 1, len(arr)):
            if arr[current_index] > arr[next_index]:
                swap_elements(arr, current_index, next_index)

    return arr


if __name__ == "__main__":
    numbers = [5, 3, 8, 6, 7, 2]
    sorted_numbers = selection_sort(numbers)
    print(sorted_numbers)
```