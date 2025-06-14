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
