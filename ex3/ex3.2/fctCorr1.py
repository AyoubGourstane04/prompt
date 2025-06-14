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
