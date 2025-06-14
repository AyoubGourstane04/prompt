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
