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
