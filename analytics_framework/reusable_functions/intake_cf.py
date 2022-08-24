import intake
from analytics_framework import INTAKE_LOC
from pathlib import Path

CATALOG_LOC = Path.joinpath(INTAKE_LOC, "catalog_entry.yml")


def initiate_catalog():
    catalog = intake.open_catalog(CATALOG_LOC)
    return catalog


def list_catalog_entry():
    return list(catalog)


def view_catalog(catalog):
    intake_app = intake.gui
    intake_app.add(catalog)
    return intake_app
