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
