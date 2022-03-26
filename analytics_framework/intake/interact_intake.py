import intake

CATALOG_PATH = "analytics_framework/intake/catalog_entry.yml"


def catalog_init():
    """
    Simple words: Opening a book, here the book is CATALOG_PATH
    Returns: Intake catalog object
    """
    catalog = intake.open_catalog(CATALOG_PATH)
    return catalog
