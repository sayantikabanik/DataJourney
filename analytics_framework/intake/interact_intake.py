from analytics_framework import intake

CATALOG_PATH = "catalog_entry.yml"


def catalog_init():
    """
    Simple words: Opening a book, here the CATALOG_PATH
    Returns: Intake catalog object
    """
    catalog = intake.open_catalog(CATALOG_PATH)
    return catalog
