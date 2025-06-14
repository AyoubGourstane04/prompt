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

