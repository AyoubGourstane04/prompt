import pytest
from prompt1 import format_product_code as format_product_code_prompt1
from prompt2 import format_product_code as format_product_code_prompt2
from prompt3 import format_product_code as format_product_code_prompt3

# Tests pour prompt1
def test_valid_product_code_prompt1():
    assert format_product_code_prompt1("ABC1234XYZ") == "ABC-1234-XYZ"

def test_invalid_length_prompt1():
    with pytest.raises(ValueError, match="Le product_id doit être une chaîne de 10 caractères alphanumériques."):
        format_product_code_prompt1("SHORT")

def test_invalid_characters_prompt1():
    with pytest.raises(ValueError):
        format_product_code_prompt1("ABC!23@XYZ")  # Contient des caractères non alphanumériques

# Tests pour prompt2
def test_valid_product_code_prompt2():
    assert format_product_code_prompt2("ABC123DEF4") == "ABC-123-DEF4"
    assert format_product_code_prompt2("XYZ987GHIJ") == "XYZ-987-GHIJ"

def test_invalid_length_prompt2():
    with pytest.raises(ValueError, match="Le product_id doit être une chaîne de 10 caractères alphanumériques."):
        format_product_code_prompt2("SHORT")

def test_invalid_characters_prompt2():
    with pytest.raises(ValueError):
        format_product_code_prompt2("XYZ@87GHIJ")  # Contient des caractères non alphanumériques

# Tests pour prompt3 (identique à prompt2 mais regroupé ici)
def test_valid_product_code_prompt3():
    assert format_product_code_prompt3("ABC123DEF4") == "ABC-123-DEF4"
    assert format_product_code_prompt3("XYZ987GHIJ") == "XYZ-987-GHIJ"

def test_invalid_length_prompt3():
    with pytest.raises(ValueError, match="Le product_id doit être une chaîne de 10 caractères alphanumériques."):
        format_product_code_prompt3("SHORT")

def test_invalid_characters_prompt3():
    with pytest.raises(ValueError):
        format_product_code_prompt3("XYZ@87GHIJ")  # Contient des caractères non alphanumériques
