import intake
import pandas as pd

from dagster import get_dagster_logger, job, op, Output, graph
from analytics_framework import INTAKE_LOC

from dagster.utils.log import get_dagster_logger
logger = get_dagster_logger()


@op
def read_catalog_data():
    catalog_path = INTAKE_LOC.joinpath("catalog_entry.yml")
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.address_sample.read()
    print(df_raw.head())
    return df_raw

@op
def



@job
def compute():
    df_raw = read_catalog_data()


if __name__ == "__main__":
    result = compute.execute_in_process()