import intake
from dagster import get_dagster_logger, job, op, Output, graph
from analytics_framework import INTAKE_LOC

from dagster.utils.log import get_dagster_logger
logger = get_dagster_logger()

catalog_path = INTAKE_LOC.joinpath("catalog_entry.yml")

@op
def read_stock_price_data():
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.twilio_stock_price.read()
    logger.info(f"Raw dataset first 05 rows: {df_raw.head(5)}")
    logger.info(f"Shape of the data loaded: {df_raw.shape}")
    return df_raw


@op
def clean_column_names(df_raw):
    df_twlo_clean = df_raw.rename(
                        columns={'1. open': 'open',
                                 '2. high': 'high',
                                 '3. low': 'low',
                                 '4. close': 'close',
                                 '5. volume': 'volume'}, inplace=False)
    logger.info(f"Updated dataframe: {df_twlo_clean.describe()}")
    return df_twlo_clean


@job
def compute():
    df_raw = read_stock_price_data()
    df_updated = clean_column_names(df_raw)


if __name__ == "__main__":
    result = compute.execute_in_process()
