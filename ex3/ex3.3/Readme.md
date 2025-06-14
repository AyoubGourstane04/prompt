## Exercice 3.3 :

**Code de fonction :** `function.py`

```python
def get_user_permissions(user_id, system_context): 
# This function fetches user permissions 
# Needs better documentation 
    if user_id in system_context['admins']: 
        return ['read', 'write', 'delete', 'admin'] 
    elif user_id in system_context['editors']: 
        return ['read', 'write'] 
    else: 
        return ['read']
```

### 1- Generation de docstring :

**Prompt :**

> "Pour la fonction suivante get_user_permissions, rédigez un docstring complet, bien structuré et conforme à un standard de documentation
> Le docstring doit :
>
> *   Décrire clairement le but de la fonction.
> *   Documenter ses paramètres : user_id et system_context.
> *   Spécifier sa valeur de retour (type et contenu).
> *   Fournir un exemple d'utilisation illustrant le comportement de la fonction.
>
> La fonction :
>
> ```python
> def get_user_permissions(user_id, system_context): 
>     # This function fetches user permissions 
>     # Needs better documentation 
>         if user_id in system_context['admins']: 
>             return ['read', 'write', 'delete', 'admin'] 
>         elif user_id in system_context['editors']: 
>             return ['read', 'write'] 
>         else: 
>             return ['read']
> ```
> "

**Résultat :**

```python
def get_user_permissions(user_id, system_context):
    """
    Détermine les permissions attribuées à un utilisateur en fonction de son rôle dans le système.

    Args:
        user_id (str): Identifiant unique de l'utilisateur.
        system_context (dict): Dictionnaire contenant les rôles des utilisateurs, avec les clés 
            'admins' et 'editors' associées à des listes d'identifiants.

    Returns:
        list: Liste des permissions accordées à l'utilisateur.
            - 'admin' : Accès complet, incluant la suppression et la gestion administrative.
            - 'write' : Permission de modification du contenu.
            - 'read' : Accès en lecture seule.

    Exemple:
        >>> system = {'admins': ['user1', 'user2'], 'editors': ['user3', 'user4']}
        >>> get_user_permissions('user1', system)
        ['read', 'write', 'delete', 'admin']
        >>> get_user_permissions('user3', system)
        ['read', 'write']
        >>> get_user_permissions('user5', system)
        ['read']
    """
    if user_id in system_context['admins']:
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context['editors']:
        return ['read', 'write']
    else:
        return ['read']
```

### 2- Géneration d'une section en Markdown pour le fichier README.md

**Prompt :**

> "Génère une section en Markdown destinée au fichier README.md d’un projet Python, qui explique comment utiliser la fonction get_user_permissions.
>
> Cette section doit inclure :
>
> *   Une description claire de la fonction et de son objectif.
> *   Les prérequis, notamment le format attendu pour l’argument system_context (expliquer la structure du dictionnaire et les clés attendues).
> *   Des exemples d’appels à la fonction avec différents cas d’utilisation, illustrant les résultats attendus.
>
> Rédige la section de manière claire, concise et adaptée à un développeur qui découvre cette fonction."

**Résultat :**

```markdown
## Utilisation de la fonction `get_user_permissions`
### Description
La fonction `get_user_permissions` permet de récupérer les permissions d'un utilisateur en fonction de son rôle dans le système. Elle vérifie l'identifiant de l'utilisateur (`user_id`) dans un dictionnaire de contexte (`system_context`) et retourne une liste de permissions.

### Prérequis
La fonction requiert un **dictionnaire `system_context`** contenant au moins les clés suivantes :
- **`admins`** : Liste des identifiants des utilisateurs ayant les droits administratifs.
- **`editors`** : Liste des identifiants des utilisateurs ayant les droits de modification.

Chaque utilisateur peut appartenir à **l'une de ces catégories ou aucune**, ce qui affecte les permissions renvoyées.

### Exemple d'utilisation

#### Définition du contexte système :
```python
system_context = {
    'admins': ['user1', 'user2'],
    'editors': ['user3', 'user4']
}
```

### 3- Après la lecture de docstring et la section README générés :

Après lecture, le docstring et la section README sont clairs, complets et faciles à comprendre. Le docstring explique bien le but, les paramètres, le retour et donne un exemple. La section README détaille le format attendu et propose des exemples concrets. Le tout est bien structuré et accessible, facilitant la compréhension pour tout développeur.